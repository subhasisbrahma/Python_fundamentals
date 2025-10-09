"""Encrypts a file using the Caesar Cipher (shift=3) for lowercase letters only."""

import string

def create_cipher_dict(shift):
    """
    Creates the Caesar Cipher mapping dictionary for lowercase letters.
    """
    lowercase_letters = string.ascii_lowercase
    return {lowercase_letters[i]: lowercase_letters[(i + shift) % 26]
            for i in range(len(lowercase_letters))}

def encrypt_file(input_filename, output_filename, shift):
    """
    Encrypts the contents of a file using the Caesar Cipher.
    Only lowercase letters are encrypted; other characters remain unchanged.
    """
    cipher_map = create_cipher_dict(shift)
    translation_table = str.maketrans(cipher_map)

    print(f"Encrypting '{input_filename}' with shift {shift}...")

    # Open input and output files using context manager
    with open(input_filename, "r") as f_in, open(output_filename, "w") as f_out:
        file_content = f_in.read()
        encrypted_content = file_content.translate(translation_table)
        f_out.write(encrypted_content)

    print(f"Encryption successful. Output written to '{output_filename}'")

encrypt_file("../PYTHON_FUNDAMENTALS/14_FILE_HANDLING/fictional_story.txt", "enc_fictional_story.txt", 3)


#f.seek() :- Takes us to the mentioned part of the file. It doesn't go directly. It goes linearly. So, if the file is big it will take time.