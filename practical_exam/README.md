# E-Library Data Insights Dashboard

## Project Overview

The **E-Library Data Insights Dashboard** is a Python-based data analysis and visualization project designed to extract meaningful insights from a library transaction dataset. It provides statistical summaries, filtering capabilities, and visual reports using popular data science libraries.

---

## Features

### 1. Dataset Loading

- Load CSV-based library transaction data
- Handles file errors gracefully

### 2. Statistical Analysis

- Average borrowing duration
- Genre-wise borrowing insights
- Top users based on borrowing duration
- Total borrowings per book

### 3. Data Filtering

Filter transactions based on:

- Date
- Genre
- User ID

### 4. Visual Reports

Generates a complete dashboard with:

- **Bar Chart** → Top 5 borrowed books
- **Line Chart** → Yearly borrowing trend
- **Histogram** → Distribution of borrowings by genre
- **Heatmap** → Borrowing activity (Day vs Month)

---

## Technologies Used

- Python
- pandas
- numpy
- matplotlib
- seaborn

---

## Project Structure

```
project/
│
├── main.py                # Menu-driven interface
├── helper.py              # LibraryDashboard class
├── dataset/
│   └── library_transactions.csv
└── README.md
```

---

## How to Run

1. Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

2. Run the practical_exam file:

```bash
python .\practical_exam\practical_exam.py
```

3. Follow the menu:

```
1. Load Dataset
2. Generate statistics summary
3. Filter Transaction
4. Generate Report
5. Exit
```

---

## Dataset Description

The dataset contains the following columns:

- Transaction ID
- Date (YYYY-MM-DD)
- User ID
- Book Title
- Genre
- Borrowing Duration (Days)

---

## Important Notes

- Ensure the dataset path is correct before loading
- Convert `Date` column to datetime for accurate analysis:

```python
df["Date"] = pd.to_datetime(df["Date"])
```

- Column names must match exactly (case-sensitive)

---

## Learning Outcomes

This project helps you understand:

- Data cleaning and preprocessing
- GroupBy operations in pandas
- Data visualization techniques
- Building a modular Python project
- Creating interactive CLI applications

---

## Conclusion

This project demonstrates a complete data analysis workflow—from loading data to generating insights and visualizations—making it a strong addition to any data science portfolio.

---
