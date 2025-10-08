"""Implements a basic, educational version of the Selection Sort algorithm

by repeatedly finding the minimum element, appending it to a new list,

and removing it from the source."""



def selection_sort_manual(input_list):

    """

    Sorts a list by manually selecting the minimum element in each pass.

    

    Parameters:

        input_list (list): The list to be sorted.

        

    Returns:

        list: A new list containing the elements in ascending order.

    """

    

    # Use .copy() to avoid modifying the original list

    unsorted_list = input_list.copy() 

    sorted_list = []



    # Loop until the unsorted list is empty

    while len(unsorted_list) > 0:

        # Find the minimum element

        minimum_element = min(unsorted_list)

        # Append to the sorted list

        sorted_list.append(minimum_element)

        # Remove from unsorted list

        unsorted_list.remove(minimum_element)

        

    return sorted_list



def demonstrate_selection_sort():

    """

    Demonstrates the selection_sort_manual function with a test list.

    """

    original_data = [99, 10, 2, 55, 390, 0, -5]

    

    print(f"Data before sorting: {original_data}")

    

    # Call the sorting function

    sorted_result = selection_sort_manual(original_data)

    

    print(f"Sorted Result: {sorted_result}")


    # Output: [-5, 0, 2, 10, 55, 99, 390]



# Execute demonstration

demonstrate_selection_sort()

