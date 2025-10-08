"""Implements a user-defined function to find the smallest element in a list
using an iterative approach."""

def find_minimum_element(input_list):
    """
    Finds the minimum numerical element in a list without using the built-in min() function.
    
    Parameters:
        input_list (list): The list of numbers to search through.
        
    Returns:
        The smallest element found in the list, or None if the list is empty.
    """
    
    if not input_list:
        print("Error: Input list is empty. Cannot determine minimum element.")
        return None
        
    min_element = input_list[0]
    
    for current_element in input_list[1:]:
        if current_element < min_element:
            min_element = current_element
            
    return min_element


def demonstrate_find_minimum_element():
    """
    Demonstrates the find_minimum_element() function with multiple test cases.
    """
    test_list_a = [1, 5, 3, 5, 8, -1, 3, 4]
    test_list_b = [100, 20, 50, 10]
    test_list_c = []
    

    # Test Case A
    min_a = find_minimum_element(test_list_a)
    print(f"List A: {test_list_a}")
    print(f"Minimum: {min_a}")  # Output: -1
    
    # Test Case B
    min_b = find_minimum_element(test_list_b)
    print(f"List B: {test_list_b}")
    print(f"Minimum: {min_b}")  # Output: 10
    
    # Test Case C (Empty List Check)
    print(f"List C: {test_list_c}")
    find_minimum_element(test_list_c) # Output: Error message and None returned


# Execute demonstration
demonstrate_find_minimum_element()
