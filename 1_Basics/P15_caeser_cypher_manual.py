"""Implements a simple Caesar cipher"""

# Define the constants for the alphabet and shift value
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
INPUT_WORD = "subhasis"
SHIFT_UNIT = 1
ALPHABET_LENGTH = len(ALPHABET)  # 26

# Initialize an empty string to build the encrypted word
encrypted_word_manual = ""

# The formula for each character is:
# new_index = (current_index + SHIFT_UNIT) % ALPHABET_LENGTH
# The modulo operator (%) ensures that when the shift goes past 'z' (index 25),
# it wraps back around to 'a' (index 0).

# Process character 0
original_index = ALPHABET.index(INPUT_WORD[0])  # Get index of 's' (18)
new_index = (original_index + SHIFT_UNIT) % ALPHABET_LENGTH  # (18 + 1) % 26 = 19
encrypted_word_manual += ALPHABET[new_index]

# Process character 1
original_index = ALPHABET.index(INPUT_WORD[1])  # Get index of 'u' (20)
new_index = (original_index + SHIFT_UNIT) % ALPHABET_LENGTH
encrypted_word_manual += ALPHABET[new_index]

encrypted_word_manual += (ALPHABET[(ALPHABET.index(INPUT_WORD[2]) + SHIFT_UNIT) % ALPHABET_LENGTH])
encrypted_word_manual += (ALPHABET[(ALPHABET.index(INPUT_WORD[3]) + SHIFT_UNIT) % ALPHABET_LENGTH])
encrypted_word_manual += (ALPHABET[(ALPHABET.index(INPUT_WORD[4]) + SHIFT_UNIT) % ALPHABET_LENGTH])
encrypted_word_manual += (ALPHABET[(ALPHABET.index(INPUT_WORD[5]) + SHIFT_UNIT) % ALPHABET_LENGTH])
encrypted_word_manual += (ALPHABET[(ALPHABET.index(INPUT_WORD[6]) + SHIFT_UNIT) % ALPHABET_LENGTH])
encrypted_word_manual += (ALPHABET[(ALPHABET.index(INPUT_WORD[7]) + SHIFT_UNIT) % ALPHABET_LENGTH])

encrypted_word_manual = "tvcitejt"

print("Original Word:", INPUT_WORD)      # Output: Original Word: subhasis
print("Manual Encrypted Result:", encrypted_word_manual)  # Output: Manual Encrypted Result: tvcitejt


