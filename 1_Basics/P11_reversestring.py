"""Reverses a string entered by the user using slicing"""


full_name = "Subhasis Brahma"

# String Slicing format: string[start : end : step]

# The Reversal Trick: [::-1]
# - Omitting 'start' defaults to the beginning (index 0).
# - Omitting 'end' defaults to the end of the string.
# - The 'step' of -1 tells Python to move backward one character at a time,
#   reversing the entire string.
reversed_name = full_name[::-1]

print("Original string:", full_name)       # Output: Original string: Subhasis Brahma
print("Reversed string:", reversed_name)   # Output: Reversed string: amharB sisahbuS
