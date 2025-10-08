"""Demonstrates the three main ways to pass arguments to a Python function:
Positional, Keyword, and Default arguments."""

# 1. Positional Arguments

def calculate_positional(num_a, num_b, num_c):
    """
    Arguments are mapped to parameters based purely on their position/order.
    """
    return (num_a + num_b - num_c)

# The arguments (20, 30, 40) are assigned sequentially:
# 20 goes to num_a, 30 goes to num_b, 40 goes to num_c.
positional_result = calculate_positional(20, 30, 40)
print(f"Positional Result (20 + 30 - 40): {positional_result}")
# Output: 10

# 2. Keyword Arguments

def calculate_keyword(param_c, param_b, param_a):
    """
    Arguments are mapped using the parameter's name, ignoring their order.
    """
    return (param_a + param_b - param_c)

# Arguments are specified with 'param=value'. The order does not matter.
keyword_result = calculate_keyword(param_a=20, param_b=30, param_c=40) 
print(f"Keyword Result (20 + 30 - 40): {keyword_result}")
# Output: 10

# 3. Default Arguments

def calculate_default(param_c, param_a=20, param_b=30):
    """
    Parameters can be assigned a default value, making them optional.
    Note: Parameters with defaults must be defined AFTER any non-default parameters.
    """
    return (param_a + param_b - param_c)

# Only the required positional argument (param_c) is provided. Uses defaults for a and b.
default_result_a = calculate_default(40)
print(f"Default Result A (using defaults): {default_result_a}") 
# Output: 10

# Explicit value for 'a' (10) overrides the default (20). 'b' uses default (30).
default_result_b = calculate_default(40, 10) 
print(f"Default Result B (a=10 overrides default): {default_result_b}")
# Output: 0

# All arguments are provided explicitly. Defaults are ignored.
default_result_c = calculate_default(40, 10, 20) 
print(f"Default Result C (all values explicit): {default_result_c}")
# Output: -10

# 4. Implicit Return of None

def print_message(message):
    """
    A function that performs an action (prints) but has no explicit 'return' statement.
    """
    print(f"Action: {message}")
    # Implicitly returns None.


# Assign the function call result to a variable.
none_return_value = print_message("Function executed.")

# Check the value captured by the variable.
print(f"Return Value (Type): {type(none_return_value)}")
print(f"Return Value (Value): {none_return_value}")
# Output: Return Value (Value): None
