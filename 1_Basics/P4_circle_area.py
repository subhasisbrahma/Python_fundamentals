"""Calculates the area of a circle using the radius provided by the user."""

PI_VALUE = 3.14

# Get the radius from the user.
# The input is immediately converted to an integer (int) for calculation.
radius = int(input("Enter the radius of the circle: "))

# The double asterisk (**) is the exponentiation operator (power of).
area = PI_VALUE * (radius ** 2)

# Print the final result. Using an f-string is the cleanest way to output variables.
print("The area of the circle is: ",area)
# Example Output if user enters '5': The area of the circle is: 78.5