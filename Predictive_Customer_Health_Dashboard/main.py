import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# --- DATA PREPARATION (Logical Code Untouched) ---
df = pd.read_csv("customer_churn_business_dataset.csv")
df["complaint_type"] = df["complaint_type"].fillna("None")

# Find product engagement
weekly_active_days_percentage = df["weekly_active_days"] * 100 / 7
usage_growth_rate_percentage = df["usage_growth_rate"] * 100
total_features_used_percentage = round(df["features_used"].max())
features_used_percentage_percentage = (
    df["features_used"] * 100 / total_features_used_percentage
)

df["product_engagement"] = (
    (weekly_active_days_percentage * 33.33)
    + (usage_growth_rate_percentage * 33.33)
    + (features_used_percentage_percentage * 33.33)
) / 100

# Find customer sentiment
csat = df["csat_score"] / 5
nps = df["nps_score"] / 100
support = 1 - np.clip(df["support_tickets"] / df["support_tickets"].max(), 0, 1)
customer_sentiment = (csat + nps + support) / 3
df["customer_sentiment_score"] = customer_sentiment * 100

# Find financially Reliability
payment_failure_score = 1 - np.clip(
    df["payment_failures"] / df["payment_failures"].max(), 0, 1
)
contract_type_df = pd.DataFrame(
    {"contract_type": ["Monthly", "Quarterly", "Yearly"], "rate": [0.2, 0.6, 1]}
)
contract_type_score = df["contract_type"].map(
    lambda x: contract_type_df[contract_type_df["contract_type"] == x]["rate"].values[0]
)
df["financial_reliability_score"] = (
    ((payment_failure_score + contract_type_score)) * 100 / 2
)
df["price_risk_modifier"] = np.where(df["price_increase_last_3m"] == 1, 0.8, 1.0)
df["financial_reliability_score"] = (
    df["financial_reliability_score"] * df["price_risk_modifier"]
)

# Find Recency
max_days = 30
df["recency_score"] = 1 - np.clip(df["last_login_days_ago"] / max_days, 0, 1)
df["recency_score"] = df["recency_score"] * 100

# Final Health Score
df["customer_health_score"] = (
    (df["product_engagement"] * 0.40)
    + (df["customer_sentiment_score"] * 0.25)
    + (df["financial_reliability_score"] * 0.20)
    + (df["recency_score"] * 0.15)
)
df["customer_health_score"] = df["customer_health_score"].round(2)

# --- UI SETUP ---
st.set_page_config(page_title="Customer Health AI", layout="wide")

# Custom CSS for styling titles
st.markdown(
    """
    <style>
    .main-title { font-size: 60px; font-weight: bold; color: #FFFFFF; margin-bottom: 0px; }
    .sub-text { font-size: 36px; color: #A0A0A0; margin-bottom: 30px; }
    .section-header { font-size: 36px; font-weight: bold; margin-top: 20px; margin-bottom: 10px; border-bottom: 1px solid #4f4f4f; padding-bottom: 5px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# 1. Header Section
st.markdown(
    '<p class="main-title">Customer Health & Churn Predictor</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="sub-text">Predictive monitoring of engagement, sentiment, and financial stability.</p>',
    unsafe_allow_html=True,
)

st.markdown('<p class="section-header">Individual Lookup</p>', unsafe_allow_html=True)
selected_id = st.selectbox(
    "Search Customer ID for Deep-Dive",
    options=df["customer_id"].unique(),
    index=None,
    placeholder="Select or type Customer ID...",
)
# 3. Individual Lookup Display (Conditional)
if selected_id:
    st.markdown(
        f'<p class="section-header">Profile: {selected_id}</p>',
        unsafe_allow_html=True,
    )
    selected_customer_detail = df[df["customer_id"] == selected_id]
    st.dataframe(selected_customer_detail, use_container_width=True, hide_index=True)
st.write("\n")
st.write("\n")

st.markdown(
    '<p class="section-header">Global Risk Threshold</p>', unsafe_allow_html=True
)
risk_threshold = st.slider("Define Churn Risk (Health Score < X)", 0, 100, 40)
# Logic for filtered data based on threshold
customer_above_threshold = df[df["customer_health_score"] < risk_threshold]
damage_in_monthly_income = customer_above_threshold["monthly_fee"].sum()
damage_in_total_revenue = customer_above_threshold["total_revenue"].sum()


# 4. Financial Impact Metrics
st.markdown(
    '<p class="section-header">Aggregate Revenue at Risk</p>', unsafe_allow_html=True
)
m1, m2 = st.columns(2)
m1.metric(
    label="Monthly Income at Risk",
    value=f"${damage_in_monthly_income:,.0f}",
    delta="Risk Exposure",
    delta_color="inverse",
)
m2.metric(
    label="Total Contract Revenue at Risk",
    value=f"${damage_in_total_revenue:,.0f}",
    delta="Total Liability",
    delta_color="inverse",
)

# 5. Visualizations
st.markdown(
    '<p class="section-header">Diagnostic Insights (High Risk Segment)</p>',
    unsafe_allow_html=True,
)
fig, ax = plt.subplots(1, 2, figsize=(16, 5))

# --- PILLAR CHART ---
pillar_names = ["Engagement", "Sentiment", "Finance", "Recency"]
pillar_values = [
    customer_above_threshold["product_engagement"].mean(),
    customer_above_threshold["customer_sentiment_score"].mean(),
    customer_above_threshold["financial_reliability_score"].mean(),
    customer_above_threshold["recency_score"].mean(),
]

ax[0].bar(
    pillar_names, pillar_values, color=["#4C72B0", "#55A868", "#C44E52", "#8172B2"]
)
for name, value in zip(pillar_names, pillar_values):
    ax[0].text(x=name, y=value + 2, s=f"{value:.1f}", ha="center", fontweight="bold")
ax[0].set_ylim(0, 115)
ax[0].set_ylabel("Average Score")
ax[0].set_title("Health Pillar Breakdown")

# --- CONTRACT CHART ---
contract_types = ["Monthly", "Quarterly", "Yearly"]
contract_values = [
    customer_above_threshold[customer_above_threshold["contract_type"] == c][
        "customer_health_score"
    ].mean()
    for c in contract_types
]

ax[1].bar(contract_types, contract_values, color=["#4C72B0", "#55A868", "#C44E52"])
for name, value in zip(contract_types, contract_values):
    ax[1].text(x=name, y=value + 2, s=f"{value:.1f}", ha="center", fontweight="bold")
ax[1].set_ylim(0, 115)
ax[1].set_title("Avg Health by Contract Type")

plt.tight_layout()
st.pyplot(fig)

st.write("\n")
st.write("\n")
# 6. Priority Data Table
st.markdown(
    f'<p class="section-header">Priority Intervention List (Health < {risk_threshold})</p>',
    unsafe_allow_html=True,
)
st.dataframe(
    customer_above_threshold[
        [
            "customer_id",
            "customer_health_score",
            "monthly_fee",
            "last_login_days_ago",
            "support_tickets",
            "contract_type",
        ]
    ].sort_values(by="customer_health_score"),
    use_container_width=True,
    hide_index=True,
)
