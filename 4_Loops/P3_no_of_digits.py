"""Count the number of digits in an integer."""

# --- Solution 1: Mathematical Approach ---

input_number = abs(int(input("Enter the number (Mathematical Method): ")))

if input_number == 0:
    print("Digit count: 1")
else:
    digit_count = 0
    current_num = input_number
    while current_num > 0:
        current_num = current_num // 10
        digit_count += 1
    print("Original Number:", input_number, ", Digit count:", digit_count)


# --- Solution 2: String Conversion Approach ---

input_number = abs(int(input("Enter the number (String Method): ")))
number_as_string = str(input_number)
digit_count = 0
for digit in number_as_string:
    digit_count += 1

print("Original Number:", input_number, ", Digit count:", digit_count)
