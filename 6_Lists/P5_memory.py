"""Demonstrates how list memory allocation and references work."""

# 1. Immutable Assignment (Integer) 

first_number = 5
second_number = first_number  # 'second_number' now holds the value 5

# Reassigning 'first_number' creates a new integer object (10) and points 'first_number' to it.
first_number = 10 

# 'second_number' still points to the original object (5).
print(f"X: {first_number}, Y: {second_number}")  # Output: 10 5


# 2. Mutable Assignment (List - Alias) 

list_one = [1, 2, 3]
list_alias = list_one  # list_alias now points to the same list object as list_one

# Modifying the object via list_one affects the object seen by list_alias
list_one[0] = 100

print(f"List 1: {list_one}")      # Output: [100, 2, 3]
print(f"List Alias: {list_alias}")  # Output: [100, 2, 3]


# 3. Safe Mutable Copying (Shallow Copy) 

original_list = [1, 2, 3]

# Three common methods to create a new list object (shallow copy)
copy_a = list(original_list)
copy_b = original_list[:]
copy_c = original_list.copy()

# Modifying the copies does NOT affect the original list
copy_a[0] = 100
copy_b[0] = 200
copy_c[0] = 300

print(f"Original: {original_list}")   # Output: [1, 2, 3]
print(f"Copy A (list()): {copy_a}")   # Output: [100, 2, 3]
print(f"Copy B ([:] slice): {copy_b}")# Output: [200, 2, 3]
print(f"Copy C (.copy()): {copy_c}")  # Output: [300, 2, 3]


# 4. Object Identity Check ('is' operator) 

original_list = [1, 2, 3]
alias_list = original_list

# Copies (create a new object)
copy_list_a = list(original_list)
copy_list_b = original_list[:]

print(f"Original is list(Original): {original_list is copy_list_a}")  # False
print(f"Original is Original[:]: {original_list is copy_list_b}")     # False
print(f"Original is Alias: {original_list is alias_list}")            # True


# 5. Function Call Behavior (Immutable vs Mutable) 

# Immutable (int) behavior (Pass-by-Value effect)
global_int = 5
x = global_int
x = x + 1  # Creates a new local object
return_int = x

print(f"Function Result: {return_int}")       # Output: 6
print(f"Global Int (Unchanged): {global_int}")# Output: 5

# Mutable (list) behavior (Pass-by-Reference effect)
global_list = [5]
global_list.append(1)
return_list = global_list

print(f"Function Result: {return_list}")     # Output: [5, 1]
print(f"Global List (CHANGED): {global_list}")# Output: [5, 1]
