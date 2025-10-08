"""Demonstrates the use of the 'global' keyword, which allows functions to directly 
read and modify a variable defined in the main (global) scope."""

# Global Variable
global_value = 5  # Accessible and modifiable across functions

# Helper Functions
def multiply_by_two_global():
    """Multiplies the global 'global_value' by 2."""
    global global_value
    global_value = global_value * 2
    print(f"Value of x inside multiply_by_two_global: {global_value}")  # Output: 10

def multiply_by_three_global():
    """Multiplies the global 'global_value' by 3."""
    global global_value
    global_value = global_value * 3
    print(f"Value of x inside multiply_by_three_global: {global_value}")  # Output: 30

def run_global_scope_demo():
    """Runs the demonstration for global variable modification."""
    print(f"Value of x before function call: {global_value}")  # Output: 5

    multiply_by_two_global()    # Modifies global_value to 10
    multiply_by_three_global()  # Modifies global_value to 30

    print(f"Value of x after function call: {global_value}")   # Output: 30

run_global_scope_demo()