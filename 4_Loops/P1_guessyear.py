"""Simple guessing game that asks the user to guess a particular year."""

CORRECT_YEAR = 1947

# Prompt for the initial input.
# The user's input is immediately converted to an integer.
entered_year = int(input("Enter the year in which INDIA got its independence: "))

# The 'while' loop continues to execute as long as the condition is True.
# The loop will break (stop executing) only when 'entered_year' equals 1947.
while entered_year != CORRECT_YEAR:
    print("Wrong. Try again!")
    # Inside the loop, the program must ask for input again.
    # This ensures the loop variable ('entered_year') has a chance to change,
    # otherwise it would become an infinite loop!
    entered_year = int(input())

# This line is executed only AFTER the loop condition (entered_year != 1947) is False.
print("Correct. Good Job!")