import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

import seaborn as sns


def plot_bar_chart(df):
    plt.subplot(2, 2, 1)

    top_borrowed_book = (
        df.groupby("Book Title")
        .size()
        .to_frame(name="Total Borrowings")
        .sort_values(by="Total Borrowings", ascending=False)
        .head(5)
    )
    plt.bar(
        top_borrowed_book.index,
        top_borrowed_book["Total Borrowings"],
        width=0.5,
        alpha=0.7,
    )

    plt.title("Top 5 Borrowed Books")
    plt.ylabel("Borrows per Book")
    plt.xlabel("Book Name")
    plt.xticks(rotation=30, ha="right")

    # Value labels
    for book_name, borrows in zip(
        top_borrowed_book.index, top_borrowed_book["Total Borrowings"]
    ):
        plt.text(book_name, borrows + 0.5, borrows, ha="center")


def plot_line_chart(df):
    plt.subplot(2, 2, 2)

    df["Year"] = pd.to_datetime(df["Date"]).dt.year

    total_borrowing_per_book = (
        df.groupby("Year").size().to_frame(name="Total Borrowings")
    )
    plt.plot(
        total_borrowing_per_book.index,
        total_borrowing_per_book["Total Borrowings"],
        marker="o",
    )

    plt.title("Yearly Borrowing Trend")
    plt.xlabel("Year")
    plt.ylabel("Total Borrowings")
    plt.xticks(total_borrowing_per_book.index)


def plot_histogram(df):
    plt.subplot(2, 2, 3)
    book_borrowed_by_genre = (
        df.groupby("Genre").size().to_frame(name="Total Borrowings")
    )
    plt.hist(
        book_borrowed_by_genre["Total Borrowings"],
        bins=10,
        label=book_borrowed_by_genre.index,
    )

    plt.title("Distribution of Book Borrowed by genre")
    plt.ylabel("Number of Genres")
    plt.ylabel("Total Borrowings")


def plot_heatmap(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Day"] = df["Date"].dt.day_name()
    df["Month"] = df["Date"].dt.month
    heatmap_data = df.pivot_table(
        index="Day", columns="Month", aggfunc="size", fill_value=0
    )
    day_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    heatmap_data = heatmap_data.reindex(day_order)
    plt.subplot(2, 2, 4)
    sns.heatmap(heatmap_data, cmap="YlGnBu", linewidths=0.5, linecolor="gray")

    plt.title("Borrowing Activity by Day and Hour")
    plt.xlabel("Month")
    plt.ylabel("Day")


class LibraryDashboard:
    df = None

    def load_data(self, file_path):
        try:
            df = pd.read_csv(file_path)
            print("\nFile loaded successfully!")

            # Check missing values
            nulls = df.isna().sum()

            if nulls.sum() > 0:
                print("\nMissing values detected:")
                print(nulls[nulls > 0])

                # Fill numeric columns with mean
                numeric_cols = self.df.select_dtypes(
                    include=["int64", "float64"]
                ).columns

                for col in numeric_cols:
                    mean_value = self.df[col].mean()
                    self.df[col].fillna(mean_value, inplace=True)

                print("\nMissing numeric values filled with column mean")

            else:
                print("\nNo missing values found in dataset")

        except FileNotFoundError as e:
            print(f"File with {file_path} path does not exist: ", e)

    def calculate_statistics(self):
        print("\n=====Basic Statistical Summary===== ")
        print(
            "- Average Borrowing Duration: ",
            self.df["Borrowing Duration"].mean(),
        )
        print("\n- Total borrowed book per genre:")
        genre_wise_total_borrowed_book = (
            self.df.groupby("Genre")["Borrowing Duration"].mean().to_frame().T
        )
        print(genre_wise_total_borrowed_book)
        print("\n- Top 5 Longest User-Borrowing Duration:")
        user_wise_total_borrowed_book = (
            self.df.groupby("User ID")["Borrowing Duration"]
            .mean()
            .sort_values(ascending=False)
            .to_frame()
            .head(5)
            .T
        )
        print(user_wise_total_borrowed_book)
        print("\n- Total Borrowing per Book:")
        total_borrowing_per_book = (
            self.df.groupby("Book Title").size().to_frame(name="Total Borrowings")
        )
        print(total_borrowing_per_book)

    def filter_transaction(self, column, condition):
        columns = self.df[self.df[column] == condition]
        if len(columns) == 0:
            print(f"\nNo data found for this {column}!")
        else:
            print(f"\nData filter by {column}:")
            print(columns)

    def generate_report(self):
        plt.figure(figsize=(12, 8))  # Create ONE figure
        # ------------------ BAR CHART ------------------

        plot_bar_chart(self.df)

        # ------------------ LINE CHART ------------------

        plot_line_chart(self.df)

        # ------------------ HISTOGRAM CHART ------------------

        plot_histogram(self.df)

        # ------------------ HEATMAP CHART ------------------

        plot_heatmap(self.df)

        # ------------------ FINAL TOUCH ------------------
        plt.tight_layout()
        plt.show()
