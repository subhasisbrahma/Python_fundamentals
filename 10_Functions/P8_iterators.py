""" the use of iterables, iterators, and the 'next()' function,
without exception handling for StopIteration."""

def demonstrate_iterator_flow():
    """
    Shows how a list (iterable) is converted to an iterator and consumed.
    """
    
    # 1. The Iterable: An object (like a list) that can be looped over.
    fruits_list = ["mango", "apple", "banana", "orange", 
                   "pineapple", "watermelon", "guava", "kiwi"]
    
    # 2. Creating the Iterator
    fruits_iterator = iter(fruits_list)

    print(f"1. First call: {next(fruits_iterator)}")   # mango
    print(f"2. Second call: {next(fruits_iterator)}")  # apple
    print(f"3. Third call: {next(fruits_iterator)}")   # banana
    
    for fruit in fruits_iterator:
        print(f"Loop element: {fruit}")  # orange, pineapple, watermelon, guava, kiwi

    # 3. StopIteration demonstration removed

def run_iterator_demo():
    """
    Function to execute the iterator demonstration.
    """
    demonstrate_iterator_flow()

# Execute demonstration
run_iterator_demo()
