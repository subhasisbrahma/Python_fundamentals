"""Implements a robust and Pythonic function to calculate the arithmetic average
(mean) of a list of numbers."""

def calculate_list_average(input_list):
    """
    Calculates the average of a list of numbers using built-in functions.
    
    Parameters:
        input_list (list): The list of numbers (int or float).
        
    Returns:
        float: The arithmetic average (mean) of the list, or None if the list is empty.
    """
    
    # Robustness Check: Prevent ZeroDivisionError if the list is empty.
    if not input_list:
        print("Error: The input list is empty. Cannot calculate average.")
        return None
    
    # Pythonic Calculation: sum of elements divided by count
    total_sum = sum(input_list)
    total_count = len(input_list)
    
    average = total_sum / total_count
    
    return average

def demonstrate_list_average():
    """
    Demonstrates the usage of calculate_list_average with multiple test cases.
    """
    test_list_a = [1, 2, 3, 4, 5]
    test_list_b = [10, 20, 30]
    test_list_c = []

    print("--- List Average Calculator ---")

    # Test Case A
    average_a = calculate_list_average(test_list_a)
    print(f"Average of {test_list_a}: {average_a}")

    # Test Case B
    average_b = calculate_list_average(test_list_b)
    print(f"Average of {test_list_b}: {average_b}")

    # Test Case C: Empty list
    calculate_list_average(test_list_c)

# Execute demonstration
demonstrate_list_average()
