import numpy as np

arr = np.array([])


def create_numpy_array():
    global arr

    print("\n--------------------------------")
    print("Select the type of array to create")
    print("--------------------------------")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        size = int(input("\nEnter the size of the array: "))
        arr = np.random.randint(0, 100, size)

        print("\nGenerated 1D Array:")
        print(arr)

    elif choice == 2:
        row = int(input("\nEnter number of rows: "))
        column = int(input("Enter number of columns: "))

        arr = np.random.randint(0, 100, [row, column])

        print("\nGenerated 2D Array:")
        print(arr)

    elif choice == 3:
        x = int(input("\nEnter number of x (depth): "))
        y = int(input("Enter number of y (rows): "))
        z = int(input("Enter number of z (columns): "))

        arr = np.random.randint(0, 100, [x, y, z])

        print("\nGenerated 3D Array:")
        print(arr)

    else:
        print("\nInvalid Choice!")
        return


def perform_math_ops():
    global arr

    print("\n--------------------------------")
    print("Choose an mathematical operations")
    print("--------------------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))

    if arr.size == 0:
        print("\nOops! No array exists. Please create an array first.")
        return

    user_arr = np.array(
        list(
            map(
                lambda x: int(x),
                input(f"\nEnter the {arr.size} elements (separated by space): ").split(
                    " "
                ),
            )
        )
    ).reshape((arr.shape))

    print("\nOriginal Array:")
    print(arr)

    print("\nSecond Array:")
    print(user_arr)

    if choice == 1:
        print("\nResult of Addition:")
        print(arr + user_arr)

    elif choice == 2:
        print("\nResult of Subtraction:")
        print(arr - user_arr)

    elif choice == 3:
        print("\nResult of Multiplication:")
        print(arr * user_arr)

    elif choice == 4:
        print("\nResult of Division:")
        print(arr / user_arr)

    else:
        print("\nInvalid choice!")
        return


def combine_split_array():
    global arr
    print("\n--------------------------------")
    print("Choose an option:")
    print("--------------------------------")
    print("1. Combine Arrays")
    print("2. Split Arrays")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        user_arr = np.array(
            list(
                map(
                    lambda x: int(x),
                    input(
                        f"\nEnter the {arr.size} elements (separated by space) to combine: "
                    ).split(" "),
                )
            )
        ).reshape((arr.shape))

        print("\nOriginal Array:")
        print(arr)

        print("\nSecond Array:")
        print(user_arr)

        print("\nResult of Combination:")
        print(np.vstack([arr, user_arr]))

    elif choice == 2:
        arrs = np.split(
            arr,
            int(input("\nEnter number of sub arrays (equal size): ")),
        )

        print("\nArray split successfully!")

        for arr in arrs:
            print(arr[0])

    else:
        print("\nInvalid choice!")
        return


def search_sort_filter_array():
    global arr
    print("\n--------------------------------")
    print("Choose an option:")
    print("--------------------------------")
    print("1. Search a value")
    print("2. Sort the array")
    print("3. Filter the values")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        val = int(input("\nEnter the value you are looking for: "))

        if val in arr:
            pos = np.argwhere(arr == val)[0]

            print("\nValue found at position:")
            print(pos)

        else:
            print("\nValue does not exist!")

    elif choice == 2:
        print("\nOriginal Array:")
        print(arr)

        print("\nSorted Array:")
        print(np.sort(arr, -1))

    elif choice == 3:
        value = int(input("\nEnter value to filter greater than: "))

        print("\nOriginal Array:")
        print(arr)

        print("\nFiltered Array:")
        print(arr[arr > value])

    else:
        print("\nInvalid choice!")
        return


def perform_agg_statistical_ops():
    global arr
    print("\n--------------------------------")
    print("Choose an aggregates / statistics:")
    print("--------------------------------")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Standard Deviation")
    print("5. Variance")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        print("\nOriginal Array:")
        print(arr)

        print("\nSum of elements:")
        print(np.sum(arr))

    elif choice == 2:
        print("\nOriginal Array:")
        print(arr)

        print("\nMean of elements:")
        print(np.mean(arr))

    elif choice == 3:
        print("\nOriginal Array:")
        print(arr)

        print("\nMedian of elements:")
        print(np.median(arr))

    elif choice == 4:
        print("\nOriginal Array:")
        print(arr)

        print("\nStandard Deviation of elements:")
        print(np.std(arr))

    elif choice == 4:
        print("\nOriginal Array:")
        print(arr)

        print("\nVariance of elements:")
        print(np.var(arr))
    else:
        print("\nInvalid choice!")
        return
