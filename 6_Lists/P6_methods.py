"""Demonstrates built-in list methods."""

# 1. Element Addition Methods

data_list = [1, 2, 3]
print("--- Element Addition ---")
print(f"Initial List: {data_list}") 

# append(value): Adds the value to the END of the list.
data_list.append(4)
print(f"After append(4): {data_list}") 

# insert(index, value): Adds the value at the specified index, shifting others right.
data_list.insert(1, 7) 
print(f"After insert(1, 7): {data_list}") 

# 2. Element Removal Methods

removal_list = [1, 2, 3, 4, 3]
print("\n--- Element Removal ---")
print(f"List for Removal: {removal_list}") 

# remove(value): Removes the FIRST occurrence of the specified value.
removal_list.remove(3) 
print(f"After remove(3): {removal_list}") 

# pop(): Removes and returns the LAST element (no arguments).
removed_element = removal_list.pop()
print(f"After pop() (removed {removed_element}): {removal_list}") 

# pop(index): Removes and returns the element at the specified index.
removed_element = removal_list.pop(0)
print(f"After pop(0) (removed {removed_element}): {removal_list}") 


# 3. Sorting and Reversing Methods

sort_list_a = [2, 6, 3, 8, 9, 1, 0, 5, 7, -7]
print("\n--- Sorting and Reversing (In-Place) ---")

# sort(): Sorts the list IN-PLACE (modifies the original list) in ascending order.
sort_list_a.sort() 
print(f"After sort() (Ascending): {sort_list_a}") 

# sort(reverse=True): Sorts the list in-place in descending order.
sort_list_b = [2, 6, 3, 8, 9, 1, 0, 5, 7, -7]
sort_list_b.sort(reverse=True) 
print(f"After sort(reverse=True): {sort_list_b}") 

# reverse(): Reverses the order of the elements IN-PLACE.
# Note: It does not sort; it just flips the current order.
sort_list_c = [2, 6, 3, 8, 9, 1, 0, 5, 7, -7]
sort_list_c.reverse() 
print(f"After reverse(): {sort_list_c}")
