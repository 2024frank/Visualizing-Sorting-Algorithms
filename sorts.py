from dataset import DataSet

def selection_sort_demo(data):
    """
        Performs selection sort on the dataset and uses the display() method to show progress.
        Parameters: data(object)
        Return None
    """
    for i in range(len(data.data) - 1):
        min_index = i
        for j in range(i + 1, len(data.data)):
            if data.data[min_index] > data.data[j]:
                min_index = j

        data.data[i], data.data[min_index] = data.data[min_index], data.data[i]
        data.display()

def merge(data, start, mid, end):
    """
        Merges two sorted halves into a single sorted segment.
        Updates the original dataset and displays progress.

        Parameters:
            data (DataSet): The dataset object containing the list to sort.
            start (int): The starting index of the left half.
            mid (int): The middle index separating the two halves.
            end (int): The ending index of the right half.

        Returns:
            None
    """
    left = data.data[start:mid + 1]
    right = data.data[mid + 1:end + 1]
    i, j, k = 0, 0, start

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            data.data[k] = left[i]
            i += 1
        else:
            data.data[k] = right[j]
            j += 1
        k += 1
        data.display()

    while i < len(left):
        data.data[k] = left[i]
        i += 1
        k += 1
        data.display()

    while j < len(right):
        data.data[k] = right[j]
        j += 1
        k += 1
        data.display()

def merge_sort(data, start, end):
    """
        Recursively splits and sorts the dataset using merge sort.

        Parameters:
            data (DataSet): The dataset object containing the list to sort.
            start (int): The starting index of the segment to sort.
            end (int): The ending index of the segment to sort.

        Returns:
            None
    """
    if start < end:
        mid = (start + end) // 2
        merge_sort(data, start, mid)
        merge_sort(data, mid + 1, end)
        merge(data, start, mid, end)

def merge_sort_demo(data):
    """
        Wrapper function for merge sort to start sorting the dataset.

        Parameters:
            data (DataSet): The dataset object containing the list to sort.

        Returns:
            None
    """
    merge_sort(data, 0, len(data.data) - 1)

def insertion_sort_demo(data):
    """
        Performs insertion sort on the dataset and uses the display() method to show progress.
        Parameters: data(object)
        returns none
    """
    for i in range(1, len(data.data)):
        key = data.data[i]
        j = i - 1
        while j >= 0 and key < data.data[j]:
            data.data[j + 1] = data.data[j]
            j -= 1
        data.data[j + 1] = key
        data.display()

def bubble_sort_demo(data):
    """
        Performs bubble sort on the dataset and uses the display() method to show progress.
        Parameters: data(object)
        Return None
    """
    for end in range(len(data.data) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if data.data[i] > data.data[i + 1]:
                swapped = True
                data.data[i], data.data[i + 1] = data.data[i + 1], data.data[i]
        data.display()
        if not swapped:
            return

def demo_test(dataset, demo):
    """
        Tests a sorting visualization by running it on a dataset object.
        Parameters: dataset (DataSet): DataSet object containing data to be sorted.
                    demo_name (str): The name of the sorting algorithm being tested.
                    demo (function): The sorting demo to be tested. 
        Return Value: None
    """
    sep = "*" * 79
    underline = "-" * 79
    print(sep)
    print("Testing", demo.__name__)
    print(underline)
    print("Initial data values:")
    print(dataset)

    print("Sorted:", dataset.is_sorted())  # Check if the data is sorted initially
    print("Running demo...")
    demo(dataset)  # Run the sorting demo
    print("Demo complete.")
    print("Sorted:", dataset.is_sorted())  # Check if the data is sorted after demo

if __name__ == "__main__":
    test_data = DataSet(10, 0, 10)
    test_data.set_data([8, 6, 4, 2, 0, 1, 3, 5, 7, 9])
    demo_test(test_data, merge_sort_demo)