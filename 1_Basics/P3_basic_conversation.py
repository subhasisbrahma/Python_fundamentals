"""Simple interactive program that takes user input and responds using print statements."""

# 1. Get User's Name
print("Hi! What's your Name?")
# input() returns a string by default, so explicit str() conversion is optional
user_name = input()

# 2. Get User's Location
print("Hello",user_name,"!","Where are you from?")
user_place = input()
print("Great!")

# 3. Get User's Age
# The input is converted to an integer (int) for future calculations.
print("By the way",user_name,",","What's your age?")
user_age = int(input())


# 4. Final Output Summary
print("Good to know that you are",user_age,"years old")

# Farewell message using the collected information.
print("Next time we meet, Bring the famous dish of",user_place,"Bye! See you")
# Example Output: Next time we meet, bring the famous dish of Delhi. Bye! See you.