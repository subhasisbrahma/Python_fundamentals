"""Demonstrates a Python generator function using the 'yield' keyword.
Generators create iterators that produce values lazily (one at a time),
saving memory, especially for large sequences."""

def generate_powers(limit):
    """
    Generator function that yields the square and then the cube of each number 
    from 0 up to (limit - 1).
    
    Parameters:
        limit (int): The upper bound (exclusive) for the sequence.
        
    Yields:
        int: The square (x*x) and then the cube (x*x*x) of the current number.
    """
    current_number = 0
    while current_number < limit:
        yield current_number * current_number      # Square
        yield current_number * current_number * current_number  # Cube
        current_number += 1

def run_generator_demo():
    """
    Creates the generator and demonstrates consuming its values.
    """
    power_generator = generate_powers(5)
    
    
    # Each pair of prints corresponds to one number's square and cube
    print(next(power_generator), next(power_generator))  # 0, 0
    print(next(power_generator), next(power_generator))  # 1, 1
    print(next(power_generator), next(power_generator))  # 4, 8
    print(next(power_generator), next(power_generator))  # 9, 27
    print(next(power_generator), next(power_generator))  # 16, 64
    

# Execute the demonstration
run_generator_demo()
