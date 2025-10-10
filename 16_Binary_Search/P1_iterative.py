"""Implements the Binary Search algorithm iteratively. Binary search is highly efficient 
(O(log n)) but requires the input list to be sorted."""

from typing import List, Any

def binary_search(sorted_list: List[Any], key: Any) -> int:
    """
    Searches for a key within a sorted list using the Binary Search algorithm.
    
    Parameters:
        sorted_list (List): The list of elements (must be sorted).
        key (Any): The value to search for.
        
    Returns:
        int: 1 if the key is found, 0 otherwise.
    """
    
    begin_index = 0
    end_index = len(sorted_list) - 1
    
    while begin_index <= end_index:
        mid_index = (begin_index + end_index) // 2
        
        if sorted_list[mid_index] == key:
            return 1
        elif sorted_list[mid_index] < key:
            begin_index = mid_index + 1
        else:
            end_index = mid_index - 1
            
    return 0 

# Test Data (must be sorted for binary search)
test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Test Case 1: Key is present (5)
search_key_present = 5
result_present = binary_search(test_data, search_key_present)
print(f"Result (Found: 1 / Not Found: 0): {result_present}")

# Test Case 2: Key is NOT present (11)
search_key_missing = 11
result_missing = binary_search(test_data, search_key_missing)
print(f"Result (Found: 1 / Not Found: 0): {result_missing}")
