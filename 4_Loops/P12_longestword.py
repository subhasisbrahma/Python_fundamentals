"""Find and print the longest word from inputs."""

EXIT_COMMAND = "-1"
max_length_found = 0

print("--- Longest Word Tracker ---")

while True:
    current_word = input("Enter a word (or enter -1 to stop): ")
    
    if current_word == EXIT_COMMAND:
        break
    
    current_length = len(current_word)
    
    if current_length > max_length_found:
        max_length_found = current_length
        print("-> New longest word found with length:", max_length_found)

print()
print("Program stopped. The length of the longest word entered was:", max_length_found)
