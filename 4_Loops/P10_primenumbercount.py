"""Prime numbers that exist within a given range."""

# Get the upper limit for checking prime numbers.
limit_number = int(input("Enter the number: "))

print()
print("Prime numbers up to", limit_number, ":")

# Handle the first prime number separately
if limit_number > 2:
    print(2, end=" ")

# Iterate through numbers from 3 up to the limit
for current_number in range(3, limit_number):
    # Check if current_number is prime
    for divisor in range(2, current_number):
        if current_number % divisor == 0:
            break
    else:
        print(current_number, end=" ")

print()  # Final newline
