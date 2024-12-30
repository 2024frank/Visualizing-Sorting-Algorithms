
# add import statements here as needed
from random import randint

class DataSet:
    """
    A class of randomly generated integers for testing sorting algorithms.

    Attributes:
        size (int): The total number of values in the dataset.
        minimum (int): The lowest value in the dataset.
        maximum (int): The highest value in the dataset.
        data (list): A list containing the values themselves.
    """

    def __init__(self, size, minimum, maximum):
        """
        Initializes the DataSet object with the given size, minimum, and maximum values.
        Automatically populates the dataset with random integers within the range.

        Parameters:
            size (int): The total number of integers in the dataset.
            minimum (int): The smallest possible integer in the dataset.
            maximum (int): The largest possible integer in the dataset.

        Returns:
            None
        """
        self.size = size
        self.minimum = minimum
        self.maximum = maximum
        self.populate_data()

    def populate_data(self):
        """
        Populates the dataset with a list of random integers.
        The list will have a length equal to `self.size`, and all integers will
        fall within the range [`self.minimum`, `self.maximum`].

        Returns:
            None
        """
        self.data = []
        for _ in range(self.size):
            self.data.append(randint(self.minimum, self.maximum))

    def get_data(self):
        """
        Returns the current dataset.

        Parameters:
            None

        Returns:
            list: The list of integers currently stored in the dataset.
        """
        return self.data

    def set_data(self, new_data):
        """
        Replaces the current dataset with the provided list of integers.
        Also updates the size, minimum, and maximum attributes to reflect the new dataset.

        Parameters:
            new_data (list of int): A list of integers to replace the current dataset.

        Returns:
            None
        """
        self.data = new_data
        self.size = len(self.data)
        self.minimum = min(self.data)
        self.maximum = max(self.data)

    def is_sorted(self):
        """
        Checks if the dataset is sorted in ascending order.

        Parameters:
            None

        Returns:
            bool: True if the dataset is sorted in ascending order or has one or no elements, False otherwise.
        """
        if len(self.data) <= 1:
            return True
        for i in range(len(self.data) - 1):
            if self.data[i] > self.data[i + 1]:
                return False
        return True

    def display(self):
        """
        Displays a simple text-based visualization of the data by printing
        values to the terminal separated by tabs and then pausing until
        the user presses Enter.

        Parameters:
            None

        Returns:
            None
        """
        print(self)
        input()

    def __str__(self):
        """
        Converts the dataset into a tab-separated string format for easy display.

        Parameters:
            None

        Returns:
            str: A string representation of the dataset where integers are separated by tabs.
        """
        result = ''
        for value in self.data:
            result += str(value) + '\t'
        return result.strip()


def make_test_section(description):
    """
    Convenience function for making the test display look nicer.

    Parameters:
        description (str): Description of what is to be tested.

    Returns:
        None
    """
    divider = "*" * 79
    underscore = "-" * 79
    print(divider)
    print(description)
    print(underscore)


def test_dataset_class():
    """
    Runs basic correctness checks for each of the DataSet class's methods.

    Parameters:
        None

    Returns:
        None
    """
    make_test_section("Testing __init__, populate_data, and get_data.")
    print("Creating dataset object with 10 values between 0 and 10.")
    test_data = DataSet(10, 0, 10)
    values = test_data.get_data()
    print("The generated values are:")
    print(values)

    make_test_section("Testing display and __str__.")
    test_data.display()

    make_test_section("Testing set_data.")
    print("Setting data to [4,1,9]")
    test_data.set_data([4, 1, 9])
    print("Display new data:")
    test_data.display()

    make_test_section("Testing is_sorted.")
    print("Sorted:", test_data.is_sorted())
    print("Setting data to [1,2,3,4]")
    test_data.set_data([1, 2, 3, 4])
    print("Sorted:", test_data.is_sorted())


if __name__ == "__main__":
    test_dataset_class()
