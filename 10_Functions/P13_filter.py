"""Demonstrates functional programming by chaining two built-in functions,
'filter' and 'map', to process data in a sequential pipeline."""

import math

# Source data containing both positive and negative numbers.
source_data = [25, -16, 9, 81, -100, 4]

# Helper Functions

def check_positive(number):
    """Filter function: Returns True only if the number is greater than 0."""
    return number > 0

def calculate_square_root(number):
    """Map function: Returns the square root of the number."""
    return math.sqrt(number)

def run_functional_pipeline():
    """
    Chains the filter and map functions to process the source data.
    """
    print("Source Data:", source_data)
    
    # Step 1: Filter positive numbers
    positive_iterator = filter(check_positive, source_data)
    
    # Step 2: Map square root function
    square_root_iterator = map(calculate_square_root, positive_iterator)
    
    # Final Result: Convert to list for display
    final_result = list(square_root_iterator)
    
    print("1. Filter (Positive numbers only): [25, 9, 81, 4]")
    print("2. Map (Square root applied):", final_result)
    # Output: [5.0, 3.0, 9.0, 2.0]

# Execute the pipeline
run_functional_pipeline()
