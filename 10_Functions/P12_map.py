"""Demonstrates the built-in 'map()' function, which applies a given function
to every item of one or more iterables and returns a map iterator."""

# Define the source lists for the mapping operations.
list_a = [10, 20, 30, 40, 50, 60]
list_b = [5, 10, 15, 20, 25, 30]

# Define the helper functions needed for the map operation.
def subtract(x, y):
    """Calculates x - y."""
    return x - y

def increment(x):
    """Calculates x + 1."""
    return x + 1

def demonstrate_map_function():
    """
    Shows how map() works with both two and one iterable inputs.
    """
    
    print("Source List A:", list_a)
    print("Source List B:", list_b)

    # 1. Mapping with TWO Iterables (Element-wise Operation)
    subtraction_iterator = map(subtract, list_a, list_b)
    subtraction_result = list(subtraction_iterator)
    print(subtraction_result)
    # Output: [5, 10, 15, 20, 25, 30]

    # 2. Mapping with ONE Iterable (Transformation Operation)
    increment_iterator = map(increment, list_a)
    increment_result = list(increment_iterator)
    print(increment_result)
    # Output: [11, 21, 31, 41, 51, 61]

# Execute the demonstration
demonstrate_map_function()
