"""Covers advanced string operations like concatenation, repetition, and formatting."""

# 1. String Replication

user_name = "Subhasis"

# The multiplication operator (*) on a string repeats the string.
print(user_name * 3)        # Output: SubhasisSubhasisSubhasis

# You can replicate a single indexed character as well.
# user_name[6] is the character 'i'.
print(user_name[6] * 3)     # Output: iii


# 2. String Comparison (Lexicographical)

country_name = "India"

# Equality Check (Case Sensitive): '=='
print(country_name == "India")  # Output: True  (Exact match)
print(country_name == "india")  # Output: False (Case mismatch: 'I' != 'i')

# Relational Comparison: Alphabetical Order
# Python compares strings character by character using ASCII/Unicode values.

# 'a' (ASCII 97) < 'o' (ASCII 111), so "apple" < "one" is True
print("apple" < "one")      # Output: True

# 'f' (ASCII 102) < 't' (ASCII 116), so "four" < "ten" is True
print("four" < "ten")       # Output: True

# If initial characters are the same, comparison moves to the next character.
# 'b' < 'z', so "ab" < "az" is True
print("ab" < "az")          # Output: True

# Comparison of different length strings with the same prefix:
# "abcdef" is compared to "abcde". Extra character 'f' makes it greater.
print("abcdef" < "abcde")   # Output: False
print("abcdef" > "abcde")   # Output: True


# 3. String Indexing

full_string = 'SubhasisBrahma'

# Positive Indexing (from 0):
print("Character at index 0:", full_string[0])     # Output: S
print("Character at index 3:", full_string[3])     # Output: h

# Negative Indexing (from -1):
print("Character at index -1:", full_string[-1])   # Output: a (last character)
print("Character at index -5:", full_string[-5])   # Output: r (5th from end)

# Accessing an index outside valid range raises IndexError
# e.g., full_string[100] would cause an error


# 4. String Slicing: [start : end : step]

# General rule: includes 'start' index, stops BEFORE 'end' index. Step defines direction.

# Slice with step=2, from index 0 to 8 (inclusive)
print("[0:9:2] (Step of 2):", full_string[0:9:2])  # Output: SbaiB
# Explanation: indices 0,2,4,6,8 → 'S','b','a','i','B'

# Slice with default start (0) up to index 7
print("[:8] (Start=0, End=7):", full_string[:8])  # Output: Subhasis
# Explanation: indices 0 through 7

# Slice with negative end index (-6), start=0
print("[:-6] (Start=0, End=-6):", full_string[:-6])  # Output: Subhasis
# Explanation: index -6 corresponds to 'B'; slice stops before -6 → last included 's'

# Reverse slice with step=-1, start=-1 (last character), end=-7 (exclusive)
print("[:-7:-1] (Reverse Step -1):", full_string[:-7:-1])  # Output: amharB
# Explanation: indices -1, -2, -3, -4, -5, -6 → 'a','m','h','a','r','B'

# Reverse slice with step=-2, start=-1, end=-7 (exclusive)
print("[-1:-7:-2] (Reverse Step -2):", full_string[-1:-7:-2])  # Output: ahr
# Explanation: indices -1, -3, -5 → 'a','h','r'

# Reverse slice with step=-2, default start=-1, end=3 (exclusive)
print("[:3:-2] (Reverse Step -2):", full_string[:3:-2])  # Output: ahrss
# Explanation:
# Start at -1 ('a'), step -2 → indices -1, -3, -5, -7, -9 → 'a','h','r','s','s'
# Stop before index 3 → final string = 'ahrss'
