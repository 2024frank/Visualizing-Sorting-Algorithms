from dataset import DataSet
from sorts import demo_test, selection_sort_demo, insertion_sort_demo,bubble_sort_demo, merge_sort_demo
import picture


class VisualDataSet(DataSet):
    """
        A subclass of DataSet that visualizes data as vertical bars on a canvas.
        Attributes:
            width (int): The width of the canvas.
            height (int): The height of the canvas.
            bar_width (int): The width of each vertical bar.
            bg_color (str): The background color of the canvas.
            fg_color (str): The foreground (bar) color.
            space (int): The space between the bars.
            margin (int): The margin around the canvas.
    """
    def __init__(self, width, height, bar_width):
        """
            Initializes a VisualDataSet object with specified canvas and bar properties.
            Parameters:
                width (int): The width of the canvas.
                height (int): The height of the canvas.
                bar_width (int): The width of each bar.
            Returns:
                None
        """
        self.margin =0  # Default margin
        self.width = width
        self.height = height
        self.bar_width = bar_width
        self.bg_color = 'skyblue'
        self.fg_color = 'lightgoldenrodyellow'
        self.space = 2

        size = (width + self.space) // (bar_width + self.space)
        minimum = int(0.05 * height)
        maximum = height

        super().__init__(size, minimum, maximum)
        self.clear_canvas()

    def clear_canvas(self):
        """
            Clears the canvas by filling it with the background color.
            Parameters: None
            Returns:
                None.
        """
        picture.set_fill_color(self.bg_color)
        picture.new_picture(self.width + 2 * self.margin, self.height + 2 * self.margin)
        picture.draw_filled_rectangle(0, 0, self.width + 2 * self.margin, self.height + 2 * self.margin)
        picture.display()


    def display(self):
        """
            Displays the dataset as a visualization with vertical bars.
            Returns:
                None
        """
        self.clear_canvas()
        x = self.margin
        for value in self.data:
            h = value
            y = self.height - h + self.margin
            w = self.bar_width
            picture.set_outline_color(self.fg_color)
            picture.set_fill_color(self.fg_color)
            picture.draw_filled_rectangle(x, y, w, h)
            x += self.bar_width + self.space
            picture.display()
        input()


def test_visualdataset_class():
    """
    Runs basic sanity checks for the VisualDataSet class.
    Parameters: None
    Return value: None
    """
    # TODO Item 1: Create a VisualDataSet object with width 600, height 400
    # and bar_width 18
    vds = VisualDataSet(640, 440,18)

    # Update margin for better visualization
    vds.margin = 10
    

    # TODO Item 2: Add code to examine the values your VisualDataSet object 
    # generated, then update the lines below to assign the correct 
    # values to actual_size, actual_lowest and actual_highest.

    actual_size = vds.size
    actual_lowest = vds.minimum
    actual_highest = vds.maximum
    
    print("Expected number of values: 30")
    print("Actual number of values:", actual_size) 
    print("The lowest value should be no lower than 20.")
    print("Actual lowest value:", actual_lowest)
    print("The highest value should be no higher than 400.")
    print("Actual highest value:", actual_highest)
    
    print("Generated values:")
    # TODO Item 3: Print the generated values to the command line
    print(vds.data)

    # TODO Item 4: Call your display method and visually inspect that it meets
    # the formatting guidelines and matches the data it represents.
    vds.display()

    print("Sorting with Selection sort")
    # TODO Item 5: Run your selection_sort_demo on your VisualDataSet object
    # and confirm that it produces a graphical visualization of Selection Sort
    selection_sort_demo(vds)


if __name__ == "__main__":
    test_visualdataset_class()
