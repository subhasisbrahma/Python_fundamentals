"""Explains Python's basic data types such as int, float, string, and boolean."""

# Define variables with descriptive names following the snake_case convention.
integer_number = 15      # Integer type (whole numbers)
float_number = 7.8       # Float type (decimal numbers)
user_name = "Subhasis"   # String type (text data)
list_of_numbers = [1, 2, 3] # List type (ordered, mutable sequence)
is_active = True         # Boolean type (True or False)
is_logged_in = False     # Boolean type (True or False)


# Use the type() function to inspect and print the class/type of each variable.

print(type(integer_number))    # Output: <class 'int'>
print(type(float_number))      # Output: <class 'float'>
print(type(user_name))         # Output: <class 'str'>
print(type(list_of_numbers))   # Output: <class 'list'>
print(type(is_active))         # Output: <class 'bool'>
print(type(is_logged_in))      # Output: <class 'bool'>


# Check the type of an individual element inside the list.
# list_of_numbers[0] accesses the first element, which is the integer 1.
print(type(list_of_numbers[0])) # Output: <class 'int'>