
from dataset import DataSet
from sorts import demo_test, selection_sort_demo, insertion_sort_demo, bubble_sort_demo,merge_sort_demo

from visualdataset import VisualDataSet

# main
def main():
    """
    The main function for the sorting algorithm visualization tool.

    This program allows users to visualize various sorting algorithms with customizable options,
    both in text-based and graphical modes. It includes the following functionalities:

    1. User Mode Selection:
       - Standard Mode: Select from four sorting algorithms and display styles.
       - Advanced Mode: Configure dataset properties and graphical settings for more control.

    2. Available Sorting Algorithms:
       - Selection Sort
       - Insertion Sort
       - Bubble Sort
       - Merge Sort

    3. visualization Options:
       - Text-based visualization: Displays the sorting process as text output.
       - Graphical visualization: Displays the sorting process as graphical bars.

    4. Standard Mode:
       - Dataset: Fixed to 15 random integers between 0 and 15.
       - Sorting Algorithm: Selected from the list provided.
       - Visualization Style: Text or graphical display.

    5. **Advanced Mode**:
       - Dataset Customization: Users can specify size, minimum, and maximum values.
       - Visualization Configuration:
           - Text: Similar text-based sorting output.
           - Graphical: Custom width, height, margin, and bar properties for the display.
           - **Margin**: The space around the graphical bars. It can be 0 or greater.

    Returns:
        None
    """
    print("""Welcome to the sorting algorithm visualization tool!
Enable advanced mode? (y/n)""")
    error = True
    while error != False:
        mode = input("Please enter your selection: ")
        try:
            if mode not in ['y', 'Y', 'N', 'n']:
                0 / 0
        except Exception:
            print(f" '{mode}' is not a valid selection. Please try again.")
        else:
            error = False
    mode = mode.lower()

    if mode == 'n':
        print("""
    The following algorithms are available:
        1: Selection Sort
        2: Insertion Sort
        3: Bubble Sort
        4: Merge sort
          """)
        error = True
        while error != False:
            option = input("Please enter your selection: ")
            try:
                if int(option) not in [1, 2, 3, 4]:
                    0 / 0
            except Exception:
                print(f" '{option}' is not a valid selection. Please try again.")
            else:
                error = False

        error = 1
        while error != 0:
            style = input("""Please select a visualization style:
                        1: Text
                        2: Graphical: """)
            try:
                if int(style) not in [1, 2]:
                    0 / 0
            except Exception:
                print(f" '{style}' is not a valid selection. Please try again.")
            else:
                error = 0

        if int(style) == 1:
            test_data = DataSet(15, 0, 15)  # Create a DataSet instance
            print("Displaying dataset as text...")
            test_data.display()  # Call the original display method
            if int(option) == 1:
                demo_test(test_data, selection_sort_demo)
            elif int(option) == 2:
                demo_test(test_data, insertion_sort_demo)
            elif int(option) == 3:
                demo_test(test_data, bubble_sort_demo)  # Bubble Sort
            else:
                demo_test(test_data,merge_sort_demo)
        # Graphical visualization 
        elif int(style) == 2:
            error = 1
            while error != 0:
                margin = input("Please Enter your margin: ")
                try:
                    if int(margin) <0:
                        0 / 0  
                except (ValueError, ZeroDivisionError):
                    print("Margin should be a positive integer greater than 0. Please try again.")
                else:
                    error = 0
            vds = VisualDataSet(600, 400, 18)
            vds.margin = int(margin)
            vds.display()  # 
            if int(option) == 1:
                selection_sort_demo(vds)
            elif int(option) == 2:
                insertion_sort_demo(vds)
            elif int(option) == 3:
                bubble_sort_demo(vds)
            else:
                merge_sort_demo(vds)
    else:  # advance mode'
        print("""
        Welcome to Advance mode
        The following algorithms are available:
        1: Selection Sort
        2: Insertion Sort
        3: Bubble Sort
        4: Merge Sort """)
        error = True
        while error != False:
            option = input("Please enter your selection: ")
            try:
                if int(option) not in [1, 2, 3]:
                    0 / 0
            except Exception:
                print(f" '{option}' is not a valid selection. Please try again.")
            else:
                error = False

        error = 1
        while error != 0:
            style = input("""Please select a visualization style:
                        1: Text
                        2: Graphical: """)
            try:
                if int(style) not in [1, 2]:
                    0 / 0
            except Exception:
                print(f" '{style}' is not a valid selection. Please try again.")
            else:
                error = 0

        if int(style) == 1:
            error = True
            while error != False:
                size = input("Please enter your the number of values you want to sort: (1-30) ")
                try:
                    if int(size) < 0 or int(size)>30:
                        0 / 0
                except Exception:
                    print(f" Please enter a number from (1-30)")
                else:
                    error = False

            error = True
            while error != False:
                minimum = input("Please enter your desire minimum value of values you want to sort: ")
                try:
                    if int(minimum) < 0:
                        0 / 0
                except Exception:
                    print(f" Please enter a number greater than 0")
                else:
                    error = False
            
            error = True
            while error != False:
                maximum = input("Please enter your desire miximum number of values you want to sort: ")
                try:
                    if int(maximum) <= int(minimum) :
                        0 / 0
                except Exception:
                    print(f" Please enter a number greater than {minimum}")
                else:
                    error = False
        

            test_data = DataSet(int(size), int(minimum), int(maximum))  # Create a DataSet instance
            print("Displaying dataset as text...")
            test_data.display()  # Call the original display method
            if int(option) == 1:
                demo_test(test_data, selection_sort_demo)
            elif int(option) == 2:
                demo_test(test_data, insertion_sort_demo)
            elif int(option) ==3 :
                demo_test(test_data, bubble_sort_demo)  # Bubble Sort
            else:
                demo_test(test_data,merge_sort_demo)
        # Graphical visualization 
        elif int(style) == 2:
            error = True
            while error != False:
                width = input("Enter the desired width of the display in pixels (600 - 650): ")
                try:
                    if int(width) > 650 or  int(width)< 600:
                        0 / 0
                except Exception:
                    print("Please enter a number from (600-650):")
                else:
                    error = False

            error = True
            while error != False:
                height = input("Enter the desired height of the display in pixels (500-530): ")
                try:
                    if int(height) > 530 or int(height)<500:
                        0 / 0
                except Exception:
                    print(f" Please enter a number between (500-530)")
                else:
                    error = False
            
            error = True
            while error != False:
                bar_width = input("Please enter your desire width for the bars (18-20: )")
                try:
                    if int(bar_width) > 20 or int(bar_width)< 18:
                        0 / 0
                except Exception:
                    print(f" Please enter a number from (18 -20): ")
                else:
                    error = False

            vds = VisualDataSet(600, 400, 18)
            vds.height = int(height)//2
            vds.width = int(width)//2
            vds.bar_width = int(bar_width)//2
            vds.display()  # Call the overridden display method
            if int(option) == 1:
                selection_sort_demo(vds)
            elif int(option) == 2:
                insertion_sort_demo(vds)
            elif int(option) == 3:
                bubble_sort_demo(vds)
            else:
                merge_sort_demo(vds)
        

# TODO: Don't edit below this line
if __name__ == "__main__":
    main()
