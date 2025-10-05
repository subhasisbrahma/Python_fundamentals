"""Explains escape sequences like \\n, \\t, and how they affect string output."""

# 1. Escape Sequences (Using the backslash '\')

# The backslash is used to "escape" a character, giving it a special meaning.

# Escape the quote: \' allows you to use a single quote inside a single-quoted string.
print('It\'s a beautiful day')  # Output: It's a beautiful day

# Tab space: \t inserts a horizontal tab, useful for simple alignment.
print('Subhasis.\tBrahma')      # Output: Subhasis.    Brahma

# Newline: \n inserts a line break.
print('Subhasis\nBrahma')       # Output: Subhasis\nBrahma
# Output:
# Subhasis
# Brahma


# 2. Alternative Quoting (Avoiding the need to escape)

# Python allows mixing quotes to simplify string definition.

# If the string uses a single quote ('), enclose the entire string in double quotes (").
print("It's a beautiful day")   # Output: It's a beautiful day

# If the string uses a double quote ("), enclose the entire string in single quotes (').
print('I am a student of "IIT Madras".')
# Output: I am a student of "IIT Madras".
