"""Demonstrates how to read a file line by line to search for a specific integer
(phone number)"""

def search_phone_number(FILE_NAME, TARGET_NUMBER):
    """
    Opens a file, searches for the target number, and prints the result.

    Parameters:
        FILE_NAME (str): The name of the file to search.
        TARGET_NUMBER (int): The integer value to find.
    """

    # Open the file in read mode
    with open(FILE_NAME, "r") as file:
        print(f"Searching for {TARGET_NUMBER} in '{FILE_NAME}'...")

        for line in file:
            # Remove whitespace and convert to integer
            current_number = int(line.strip())

            # Check if this is the target
            if current_number == TARGET_NUMBER:
                print("SUCCESS: The number was found")
                break
        else:
            # Executes if the loop completes without finding the number
            print("FAIL: The number was not found")

search_phone_number("../PYTHON_FUNDAMENTALS/14_File_Handling/big_phone_numbers.txt",9090909090)