"""Implements the function that returns sum of natural numbers upto "n" using Recursion"""
""" RECURSION - This method solves a problem by defining it in terms of a smaller instance of itself."""

def sum_corrected(n):
    # CORRECTED Base Case: Stop when n reaches 0
    if n == 0:
        return 0
    # Add a check for negative numbers to prevent errors
    if n < 0:
        raise ValueError("Summation is only defined for non-negative integers.")
        
    return sum_corrected(n - 1) + n

# Test the corrected function
print(sum_corrected(5))  # Output: 15
print(sum_corrected(0))  # Output: 0