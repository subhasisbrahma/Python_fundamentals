"""Demonstrates List Comprehension, the highly efficient and concise way to
create a new list by filtering and transforming elements from an existing sequence."""

source_fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]

print("Source List of Fruits:", source_fruits)

# 1. Traditional Loop (Commented out for comparison)
'''
# Traditional approach requires initialization, a loop, a conditional check,
# and an append operation across multiple lines.
filtered_list_traditional = []
for fruit in source_fruits:
    if 'n' in fruit:
        filtered_list_traditional.append(fruit.capitalize())
'''

# 2. List Comprehension (The Pythonic Way)

# Syntax: [ (expression/transformation) for (item) in (iterable) if (condition) ]
# Action:
# 1. Iterates through 'fruit' in 'source_fruits'.
# 2. Filters the list using 'if 'n' in fruit'.
# 3. Applies the transformation 'fruit.capitalize()' to the remaining items.

filtered_and_capitalized_list = [fruit.capitalize() for fruit in source_fruits if 'n' in fruit]

print(filtered_and_capitalized_list)
# Output: ['Banana', 'Orange', 'Pineapple', 'Watermelon']
