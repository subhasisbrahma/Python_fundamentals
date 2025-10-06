"""Compute the factorial of a number using a loop."""

# Get input from the user and ensure it is an integer.
number_to_factorialize = int(input("Enter the number to find its factorial: "))

# Initialize variables required for the calculation.
counter = 1
factorial_result = 1

# Check the edge case: Factorial is not defined for negative numbers.
if (number_to_factorialize < 0):
    print("Not Defined")
    # Output for -5: Not Defined

# Handle the base case (0! = 1) and all positive integers.
else:
    # The loop runs as long as the counter is less than or equal to the input number.
    while (counter <= number_to_factorialize):
        # The new factorial is the old factorial multiplied by the current counter.
        factorial_result = factorial_result * counter
        
        # Increment the counter (i = i + 1)
        counter = counter + 1
        
    # Print the final result after the loop finishes.
    print(factorial_result)
    # Example Output for 5: 120 (since 5! = 5*4*3*2*1)