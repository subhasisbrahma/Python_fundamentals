"""Demonstrates creation, access, and basic methods of a Python dictionary."""

# 1. Dictionary Creation and Assignment
user_data = {}  # Empty dictionary

# Assign values
user_data['Subhasis'] = 8
user_data['Brahma'] = 6
user_data['Cricket'] = 7

print(f"Final Dictionary: {user_data}")
# Output: {'Subhasis': 8, 'Brahma': 6, 'Cricket': 7}

# 2. Accessing Values
brahma_value = user_data['Brahma']
print(f"Value accessed by key 'Brahma': {brahma_value}")
# Output: 6

# 3. Dictionary Views

# Keys
all_keys = user_data.keys()
print(f".keys() view: {all_keys}")
# Output: dict_keys(['Subhasis', 'Brahma', 'Cricket'])

# Values
all_values = user_data.values()
print(f".values() view: {all_values}")
# Output: dict_values([8, 6, 7])

# Items
all_items = user_data.items()
print(f".items() view: {all_items}")
# Output: dict_items([('Subhasis', 8), ('Brahma', 6), ('Cricket', 7)])
