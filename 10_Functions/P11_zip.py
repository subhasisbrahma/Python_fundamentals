"""Demonstrates the built-in 'zip()' function, which combines elements from
multiple iterables (like lists) into a single sequence of corresponding tuples.
The result is then converted into a list and a dictionary."""

def demonstrate_zip_function():
    """
    Combines two lists of equal length using zip() and shows the resulting structures.
    """
    
    # Define the two lists (the iterables)
    fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]
    size = [5, 5, 6, 6, 9, 10, 5, 4]
    
    print("Source Lists:")
    print(f"Fruits: {fruits}")
    print(f"Size:   {size}")

    # 1. Converting to a List of Tuples
    list_of_pairs = list(zip(fruits, size))
    print(list_of_pairs)
    # Output: [('mango', 5), ('apple', 5), ('banana', 6), ...]

    # 2. Converting to a Dictionary
    dictionary_mapping = dict(zip(fruits, size))
    print(dictionary_mapping)
    # Output: {'mango': 5, 'apple': 5, 'banana': 6, ...}

# Execute the demonstration
demonstrate_zip_function()
