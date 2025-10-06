"""Assign a letter grade based on a numeric score using if-else conditions."""

# Get input from the user and ensure it is converted to an integer (int).
marks = int(input("Enter your marks: "))

# Validation Check: Ensures marks are within the valid range (0 to 100).
# This prevents erroneous grades from being assigned to impossible scores.
if (marks >= 0 and marks <= 100):

    # Grading Logic (Uses elif to check conditions sequentially)

    if (marks >= 90):
        print("A")
        # Output for 90-100: A

    # Only checks marks < 90 because marks >= 90 was already handled above.
    elif (marks >= 80):
        print("B")
        # Output for 80-89: B

    elif (marks >= 70):
        print("C")
        # Output for 70-79: C

    elif (marks >= 60):
        print("D")
        # Output for 60-69: D

    else:
        # If marks are valid (0-59) but fall below 60.
        print("E")
        # Output for 0-59: E

else:
    # Executes if the initial validation check fails.
    print("Invalid Marks")
    # Output for marks < 0 or marks > 100: Invalid Marks