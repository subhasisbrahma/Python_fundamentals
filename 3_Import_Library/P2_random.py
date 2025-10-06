"""Show examples of generating random numbers using Python's random module."""

import random

# 1. random.random()
# Generates a random floating-point number (float) between 0.0 (inclusive)
# and 1.0 (exclusive). This is the most basic function.
random_float = random.random()
print("Random float between 0.0 and 1.0:", random_float)
# Example Output: Random float between 0.0 and 1.0: 0.123456789...

# 2. random.randrange(start, stop)
# Generates a random integer from the range defined by 'start' (inclusive)
# up to 'stop' (exclusive). This is equivalent to rolling a die.
# The range [1, 7) means possible results are 1, 2, 3, 4, 5, 6.
random_integer = random.randrange(1, 7)
print("Random integer from 1 to 6:", random_integer)
# Example Output: Random integer from 1 to 6: 4
