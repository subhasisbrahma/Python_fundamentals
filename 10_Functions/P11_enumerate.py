"""Demonstrates the built-in 'enumerate()' function, which is used to iterate over
a sequence while keeping track of both the index (count) and the value."""

def demonstrate_enumerate():
    """
    Shows two ways to use enumerate(): first by printing the (index, value) tuple,
    and second by unpacking the tuple directly in the loop (best practice).
    """
    
    fruits_list = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]
    
    print("Source List:", fruits_list)

    # 1. Outputting the Raw Tuple
    
    for item_tuple in enumerate(fruits_list): 
        print(item_tuple)
    # Example Output: (0, 'mango'), (1, 'apple'), ...

    
    # 2. Tuple Unpacking (The Pythonic Way)
    
    for index, fruit in enumerate(fruits_list):
        print(f"Index {index}: {fruit.capitalize()}")
    # Example Output: Index 0: Mango, Index 1: Apple, ...


# Execute the demonstration
demonstrate_enumerate()
