"""Demonstrates common Python string methods such as upper(), lower(), replace(), and split()."""

# Initial string with mixed case for demonstration
mixed_case_string = "pytHoN sTrIng mEthOdS"

# 1. Case Conversion Methods (Return a new string)

lower_case = mixed_case_string.lower()      # Convert all to lowercase
upper_case = mixed_case_string.upper()      # Convert all to uppercase
capitalized = mixed_case_string.capitalize() # Capitalize only the first character, rest are lowercase
title_case = mixed_case_string.title()      # Capitalize the first letter of every word
swapped_case = mixed_case_string.swapcase()  # Invert case (upper becomes lower, lower becomes upper)

print("Lower:", lower_case)      # Output: Lower: python string methods
print("Upper:", upper_case)      # Output: Upper: PYTHON STRING METHODS
print("Capitalize:", capitalized) # Output: Capitalize: Python string methods
print("Title:", title_case)      # Output: Title: Python String Methods
print("Swapcase:", swapped_case)  # Output: Swapcase: PYThOn StRiNG MeTHoDs


# 2. Case Testing Methods (Return Boolean True/False)

# islower() requires ALL alphabetic characters to be lowercase.
print()
print(lower_case.islower())   # Output: True
print(upper_case.islower())   # Output: False

# isupper() requires ALL alphabetic characters to be uppercase.
print(upper_case.isupper())   # Output: True
print(capitalized.isupper())  # Output: False

# istitle() requires the first letter of every word to be capitalized.
print(title_case.istitle())   # Output: True


# 3. Content Testing Methods

alphanumeric_string = "abc123"

# isdigit(): True if ALL characters are numeric (0-9).
print()
print("'" + alphanumeric_string + "'.isdigit():", alphanumeric_string.isdigit()) # Output: 'abc123'.isdigit(): False

# isalpha(): True if ALL characters are alphabets (a-z, A-Z).
print("'" + alphanumeric_string + "'.isalpha():", alphanumeric_string.isalpha()) # Output: 'abc123'.isalpha(): False

# isalnum(): True if ALL characters are alphanumeric (alphabets OR numbers).
print("'" + alphanumeric_string + "'.isalnum():", alphanumeric_string.isalnum()) # Output: 'abc123'.isalnum(): True


# 4. Strip (Trim) Methods

padded_string = "----Python----"
inner_separator_string = "Python---tutorial"

# strip(): Removes specified leading and trailing characters.
print()
print("Trimmed (strip): '" + padded_string.strip('-') + "'") # Output: Trimmed (strip): 'Python'

# lstrip(): Removes specified leading (left) characters.
print("Left Trim (lstrip): '" + padded_string.lstrip('-') + "'") # Output: Left Trim (lstrip): 'Python----'

# rstrip(): Removes specified trailing (right) characters.
print("Right Trim (rstrip): '" + padded_string.rstrip('-') + "'") # Output: Right Trim (rstrip): '----Python'

# strip() does NOT remove characters that are in the middle of the string.
print("Middle separator (strip): '" + inner_separator_string.strip('-') + "'") # Output: Middle separator (strip): 'Python---tutorial'


# 5. Start/End and Search Methods

# startswith(): Checks if the string begins with the specified value (Case sensitive).
print()
print("Starts with 'P'?:", inner_separator_string.startswith('P')) # Output: True
print("Starts with 'p'?:", inner_separator_string.startswith('p')) # Output: False

# endswith(): Checks if the string ends with the specified value (Case sensitive).
print("Ends with 'L'?:", inner_separator_string.endswith('L')) # Output: False
print("Ends with 'l'?:", inner_separator_string.endswith('l')) # Output: True

# count(): Returns the number of times a specified value occurs in a string.
print()
print("Count of 't' in '" + mixed_case_string + "':", mixed_case_string.count('t')) # Output: 2

# index(): Returns the index of the first occurrence of the specified value.
# It is case-sensitive!
print("Index of 'I' (uppercase) in '" + mixed_case_string + "':", mixed_case_string.index('I')) # Output: 10

# replace(): Returns a string where all occurrences of a specified value are replaced.
replaced_string = mixed_case_string.replace('g','G')
print("Replaced 'g' with 'G':", replaced_string) # Output: pytHoN sTrInG mEthOdS
