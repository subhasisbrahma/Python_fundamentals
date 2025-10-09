"""Implements the factorial function (n!) using recursion."""

def calculate_factorial(n):
    """
    Calculates n! (n factorial) recursively.
    
    Parameters:
        n (int): The non-negative integer for which to calculate the factorial.
        
    Returns:
        int: The factorial result.
    """
    
    # 1. Base Case (Stopping Condition)
    # The recursion stops when n is 0 or 1, as 0! = 1 and 1! = 1.
    if n == 0 or n == 1:
        return 1
    
    # Optional: Error handling for negative input
    if n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
        
    # 2. Recursive Step
    # The function calls itself with a smaller input (n-1) and multiplies the result by n.
    # Example for n=5: 5 * fact(4) -> 5 * 4 * fact(3) -> ...
    return calculate_factorial(n - 1) * n

# Example usage
test_number = 5
factorial_result = calculate_factorial(test_number)

print(f"--- Recursive Factorial Demo ---")
print(f"Input: {test_number}")
print(f"Result ({test_number}!): {factorial_result}") # Output: 120 (since 5*4*3*2*1)
