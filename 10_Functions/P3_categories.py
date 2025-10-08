"""A summary and demonstration of the different types of functions in Python,
including built-in functions, module functions, string methods, and user-defined functions."""
import math
import random

# 1. User-Defined Function (UDF) Definition

def calculate_square(number):
    """
    User-Defined Function (UDF): Calculates the square of a given number.
    
    Parameters:
        number (int/float): The value to be squared.
        
    Returns:
        The result of the number multiplied by itself.
    """
    squared_result = number ** 2
    return squared_result

# 2. Function Categories Summary

# 1. Inbuilt Functions: Functions available globally without importing any modules.
print("1. Inbuilt Functions (Global): print(), input(), len(), type()")

# 2. Library Functions: Functions made available after importing a specific module.
print("2. Library Functions (Module-Specific): math.log(), math.sqrt(), random.randrange()")

# 3. String Methods: Functions that are attached to an object's data type (called using dot notation).
print("3. Object Methods (e.g., String): 'hello'.upper(), '  text  '.strip(), 'a'.replace()")


# 3. User Defined Functions Demonstration


test_number = 5
# Correct function call: Use the name 'calculate_square'
result = calculate_square(test_number) 

print(f"Calling User Defined Functions: calculate_square({test_number})")
print(f"Result: {result}")
# Output: 25
