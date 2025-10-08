"""Demonstrates the basic structure of a Python function, including the difference
between parameters and arguments, and the flow of the 'return' statement."""

def add_numbers(num_a, num_b):
    """
    Function Definition: Adds two numbers together.
    
    Parameters:
        num_a (int/float): The first number to be added.
        num_b (int/float): The second number to be added.
        
    Returns:
        The sum of the two input numbers.
    """
    # The variables 'num_a' and 'num_b' are the PARAMETERS that the function expects.
    # The 'return' statement sends the result back to the place where the function was called.
    return (num_a + num_b)

# Function Calls Demonstration

# 1. Direct call
result = add_numbers(2, 3) # The values '2' and '3' are the ARGUMENTS passed to the function.
print(f"Result of function call (add_numbers(2, 3)): {result}")
# Output: 5

# 2. Call with descriptive variables
x = 10
y = 5
sum_result = add_numbers(x, y)
print(f"Result of function call (add_numbers(10, 5)): {sum_result}")
# Output: 15
