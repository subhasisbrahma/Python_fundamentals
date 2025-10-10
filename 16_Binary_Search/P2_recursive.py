"""Implements the Binary Search algorithm using recursion. This method solves 
the problem by breaking the search down into smaller, identical search problems."""
from typing import List, Any

def rbinarysearch(sorted_list: List[Any], key: Any, begin: int, end: int) -> int:
    """
    Recursively searches for a key within a sorted list.
    
    Parameters:
        sorted_list (List): The list of elements (must be sorted).
        key (Any): The value to search for.
        begin (int): The starting index of the current search space.
        end (int): The ending index of the current search space.
        
    Returns:
        int: 1 if the key is found, 0 otherwise.
    """
    
    if begin > end:
        return 0
    
    mid_index = (begin + end) // 2
    
    if sorted_list[mid_index] == key:
        return 1
    elif sorted_list[mid_index] < key:
        return rbinarysearch(sorted_list, key, mid_index + 1, end)
    else:
        return rbinarysearch(sorted_list, key, begin, mid_index - 1)

# Test Data: MUST be sorted!
test_data = [1, 2, 3, 4, 5, 6, 7, 8]
list_length = len(test_data)

# Test Case 1: Key is present (3)
search_key_present = 3
result_present = rbinarysearch(test_data, search_key_present, 0, list_length - 1)
print(f"Searching for {search_key_present}: {result_present}") # Output: 1

# Test Case 2: Key is NOT present (10)
search_key_missing = 10
result_missing = rbinarysearch(test_data, search_key_missing, 0, list_length - 1)
print(f"Searching for {search_key_missing}: {result_missing}") # Output: 0
