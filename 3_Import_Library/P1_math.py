"""Demonstrate usage of Python's math module for common mathematical operations."""

import math

# 1. math.log(x): Calculates the natural logarithm (base e) of x.
# For log base 10, you would use math.log10(x).
natural_log = math.log(10)
print("Natural Log (ln) of 10:", natural_log)  # Output: Natural Log (ln) of 10: 2.302585092994046

# 2. math.sqrt(x): Calculates the square root of x.
square_root = math.sqrt(25)
print("Square Root of 25:", square_root)      # Output: Square Root of 25: 5.0

# 3. math.factorial(x): Calculates the factorial of x (x!).
# Factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
factorial_result = math.factorial(5)
print("Factorial of 5:", factorial_result)    # Output: Factorial of 5: 120
