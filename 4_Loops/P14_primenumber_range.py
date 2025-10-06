"""Display all prime numbers within a user-defined range."""

start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))

# Ensure start is not greater than end
if start_number > end_number:
    start_number, end_number = end_number, start_number

print()
print("Prime numbers between", start_number, "and", end_number, ":")

# Handle the prime number 2 separately
if start_number <= 2 and end_number >= 2:
    print(2, end=" ")

# Loop through all odd numbers in the range (start at 3)
for current_number in range(max(3, start_number), end_number + 1):
    if current_number % 2 == 0:
        continue

    for divisor in range(2, current_number):
        if current_number % divisor == 0:
            break
    else:
        print(current_number, end=" ")

print()
