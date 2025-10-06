"""Print simple patterns"""

numbers_to_print = [1, 11, 111, 1111, 11111]

print("--- 1. Default Formatting (No Padding) ---")
for number in numbers_to_print:
    print('{0}'.format(number))

print("\n--- 2. Fixed-Width Formatting (Padded to 5 Characters) ---")
for number in numbers_to_print:
    print('{0:5d}'.format(number))
