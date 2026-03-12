import pandas as pd
import matplotlib.pyplot as plt

df = None


def load_dataset():
    global df
    file_name = input("Enter CSV file name: ")
    try:
        df = pd.read_csv(f"./Visualization/{file_name}")
        print("Dataset Loaded Successfully!\n")

    except FileNotFoundError:
        print("File not found. Please check the file name.")


def explore_data():
    global df
    if df is None:
        print("Please load dataset first!")

    else:
        print("\n===== Explore Data Menu =====")
        print("1. View First 5 Rows")
        print("2. Dataset Shape")
        print("3. Column Names")
        print("4. Data Types")
        print("5. Summary Statistics")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            print("\nFirst 5 rows:")
            print(df.head())

        elif choice == 2:
            print("\nDataset Shape:")
            print(df.shape)

        elif choice == 3:
            print("\nColumn Names:")
            print(df.columns)

        elif choice == 4:
            print("\nData Types:")
            print(df.dtypes)

        elif choice == 5:
            print("\nSummary Statistics:")
            print(df.describe())
        else:
            print("\nInvalid choice!")


def perform_dataframe_ops():
    print("\n===== DataFrame Operations =====")
    print("1. Filter Rows")
    print("2. Sort Data")
    print("3. Add New Column")
    print("4. Delete Column")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        col = input("\nEnter column name: ")
        val = input("Enter value to filter: ")
        print(df[df[col] == val])

    elif choice == 2:
        col = input("\nEnter column name to sort by: ")
        print(df.sort_values(by=col))

    elif choice == 3:
        new_col = input("\nEnter new column name: ")
        df[new_col] = input("Enter value for column: ")
        print("Column added!")

    elif choice == 4:
        col = input("\nEnter column name to delete: ")
        df.drop(col, axis=1, inplace=True)
        print("Column deleted!")

    else:
        print("\nInvalid choice!")


def handle_missing_data():
    print("\n== Handle Missing Data ==")
    print("1. Display rows with missing values")
    print("2. Fill missing values with mean")
    print("3. Drop rows with missing values")
    print("4. Replace missing values with a specific values")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        print("\nRow with missing values:")
        rows_with_missing_values = df[df.isnull().any(axis=1)]
        print(rows_with_missing_values)

    elif choice == 2:
        rows_with_missing_values = df[df.isnull().any(axis=1)]
        df.fillna(df.mean(numeric_only=True), inplace=True)
        print("\nMissing value filled successfully!")

    elif choice == 3:
        df.dropna(axis=0, inplace=True)
        print("\nRows with missing value:")
        print(df.isnull().any(axis=1))

    elif choice == 4:
        df.fillna(0, inplace=True)
        print("\nFilled missing values!")

    else:
        print("\nInvalid choice!")


def create_charts():
    print("\n== Data Visualization ==")
    print("1. Bar Plot")
    print("2. Line Plot")
    print("3. Scatter Plot")
    print("4. Pie Plot")
    print("5. Histogram")
    print("6. Stack Plot")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:

        x = input("Enter the x-axis column name: ")
        y = input("Enter the y-axis column name: ")

        x_vals = df[x].sample(5)

        plt.bar(df[x].sample(5), df[y].sample(5), width=5)

        for i, v in enumerate(df[y].sample(5)):
            plt.text(x_vals.iloc[i], v + 2, str(v), ha="center", fontweight=2)

        plt.xlabel(x)
        plt.ylabel(y)

        save_visualization = input("\nWould you like to save visualization?(y/n)")

        if save_visualization == "y":
            file_name = input("Please enter the file name to be saved(.png): ")
            plt.savefig(f"./Visualization/{file_name}")

        plt.show()

    elif choice == 2:

        x = input("Enter the x-axis column name: ")
        y = input("Enter the y-axis column name: ")

        y_vals = df[y].sample(5)

        plt.plot(df[x].sample(5), df[y].sample(5), marker="o")

        for i, v in enumerate(df[y].sample(5)):
            plt.text(x_vals.iloc[i], v + 2, str(v), ha="center", fontweight=2)

        save_visualization = input("\nWould you like to save visualization?(y/n)")

        if save_visualization == "y":
            file_name = input("Please enter the file name to be saved(.png): ")
            plt.savefig(f"./Visualization/{file_name}")

        plt.xlabel(x)
        plt.ylabel(y)

        plt.show()

    elif choice == 3:

        x = input("Enter the x-axis column name: ")
        y = input("Enter the y-axis column name: ")

        x_vals = df[x].sample(5)

        plt.scatter(df[x].sample(5), df[y].sample(5))

        for i, v in enumerate(df[y].sample(5)):
            plt.text(x_vals.iloc[i], v + 2, str(v), ha="center", fontweight=2)

        save_visualization = input("\nWould you like to save visualization?(y/n)")

        if save_visualization == "y":
            file_name = input("Please enter the file name to be saved(.png): ")
            plt.savefig(f"./Visualization/{file_name}")

        plt.xlabel(x)
        plt.ylabel(y)

        plt.show()

    elif choice == 4:

        y = input("Enter the column name: ")
        y_vals = df[y].sample(5)

        plt.pie(y_vals, labels=y_vals.index, startangle=90, autopct="%.2f%%")
        plt.title(f"Pie Chart of {y}")

        save_visualization = input("\nWould you like to save visualization?(y/n)")

        if save_visualization == "y":
            file_name = input("Please enter the file name to be saved(.png): ")
            plt.savefig(f"./Visualization/{file_name}")

        plt.show()

    elif choice == 5:

        y = input("Enter the column name: ")
        y_vals = df[y].sample(5)

        plt.hist(y_vals, bins=10)
        plt.title(f"Pie Chart of {y}")

        save_visualization = input("\nWould you like to save visualization?(y/n)")

        if save_visualization == "y":
            file_name = input("Please enter the file name to be saved(.png): ")
            plt.savefig(f"./Visualization/{file_name}")

        plt.show()

    elif choice == 6:

        x = input("Enter the x-axis column name: ")
        y1 = input("Enter first y column: ")
        y2 = input("Enter second y column: ")

        x_vals = df[x].head(5)
        y1_vals = df[y1].head(5)
        y2_vals = df[y2].head(5)

        plt.stackplot(x_vals, y1_vals, y2_vals, labels=[y1, y2])

        plt.xlabel(x)
        plt.ylabel("Values")
        plt.legend()
        plt.title("Stack Plot")

        save_visualization = input("\nWould you like to save visualization?(y/n)")

        if save_visualization == "y":
            file_name = input("Please enter the file name to be saved(.png): ")
            plt.savefig(f"./Visualization/{file_name}")

        plt.show()

    else:
        print("\nInvalid choice!")


def describe_dataset():
    print("\nDescriptive Statistics:")
    print(df.describe())
