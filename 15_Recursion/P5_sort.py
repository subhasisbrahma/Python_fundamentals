"""Implements a recursive version of the Selection Sort algorithm.
It finds the minimum element and prepends it to the result of recursively 
sorting the remainder of the list."""

# The manual minimum function is kept here to demonstrate the logic.
def find_minimum_manual(input_list):
    """Iteratively finds the minimum element in a list."""
    min_element = input_list[0]
    for element in input_list:
        if element < min_element:
            min_element = element
    return min_element


def sort_recursively(input_list):
    """
    Sorts a list using the recursive Selection Sort method.
    
    Parameters:
        input_list (list): The list to be sorted.
        
    Returns:
        list: A new list containing the sorted elements.
    """
    
    # Base Case: The recursion stops when the list is empty or has one element.
    if len(input_list) <= 1:
        return input_list[:]

    # Recursive Step
    minimum_element = min(input_list)
    remaining_list = input_list[:]
    remaining_list.remove(minimum_element)
    
    return [minimum_element] + sort_recursively(remaining_list)


# Test data
test_data = [7, 5, 8, 3, 1, 5, 8, 5, -2, 100]

print(f"Original Data: {test_data}")

# Call the sorting function
sorted_result = sort_recursively(test_data)

print(f"Sorted Result: {sorted_result}")

# Verify that the original list was NOT mutated
print(f"Original Data After Sort (must be unchanged): {test_data}")
