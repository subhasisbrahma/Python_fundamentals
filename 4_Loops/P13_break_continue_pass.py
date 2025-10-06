"""Demonstrate the use of break, continue, and pass statements in loops."""

# --- 1. Using 'break' ---
print("--- 1. Using 'break' ---")
user_email = input("Enter your Email: ")

for current_character in user_email:
    if current_character == '@':
        print()
        print("Break encountered at '@'. Loop terminated.")
        break
    print(current_character, end='')
print()

# --- 2. Using 'continue' ---
print("\n--- 2. Using 'continue' ---")
user_email = input("Enter your Email: ")

for current_character in user_email:
    if current_character == '@':
        print("(Skipped '@' using continue)", end='')
        continue
    print(current_character, end='')
print()

# --- 3. Using 'pass' ---
print("\n--- 3. Using 'pass' ---")
for number in range(11):
    if number % 3 == 0:
        print(number, end=' ')
    else:
        pass
print()
