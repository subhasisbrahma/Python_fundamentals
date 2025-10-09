"""Implements a recursive function to check if the integer 0 exists anywhere 
within a list of numbers. Returns 1 if found, or 0 if not found."""

def contains_zero_recursive(input_list):
    """
    Recursively checks if a list contains the integer 0.
    
    Parameters:
        input_list (list): The list being checked.
        
    Returns:
        int: 1 (True) if 0 is found, 0 (False) otherwise.
    """
    
    # Base Case 1: If the list is empty, 0 was not found after checking all elements.
    if not input_list:
        return 0
        
    # Base Case 2: Check if the first element is 0. If so, return success (1).
    if input_list[0] == 0:
        return 1
        
    # Recursive Step: Call the function on the rest of the list.
    return contains_zero_recursive(input_list[1:])

# Test Case 1: Zero is NOT present
list_a = [1, 2, 3, 4, 5, 9]
result_a = contains_zero_recursive(list_a)
print(f"List: {list_a}")
print(f"Result (Found Zero): {result_a}") # Output: 0

# Test Case 2: Zero IS present
list_b = [1, 2, 3, 4, 5, 0, 9]
result_b = contains_zero_recursive(list_b)
print(f"\nList: {list_b}")
print(f"Result (Found Zero): {result_b}") # Output: 1
