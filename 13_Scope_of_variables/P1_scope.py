"""Demonstrates how local variable reassignment inside functions does not affect
the original global variable, specifically because integers are immutable types."""

# Helper Functions
def multiply_by_two(local_var):
    """Multiplies the argument by 2 within the function's local scope."""
    local_var = local_var * 2
    print(f"Value of x inside multiply_by_two: {local_var}")

def multiply_by_three(local_var):
    """Multiplies the argument by 3 within the function's local scope."""
    local_var = local_var * 3
    print(f"Value of x inside multiply_by_three: {local_var}")

def run_scope_demo():
    """Runs the demonstration for scope and immutability."""
    global_x = 5
    print(f"Value of x before function call: {global_x}")  # Output: 5

    multiply_by_two(global_x)    # Output: 10
    multiply_by_three(global_x)  # Output: 15

    print(f"Value of x after function call: {global_x}")   # Output: 5


run_scope_demo()