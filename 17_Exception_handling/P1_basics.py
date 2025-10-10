"""Demonstrates the use of 'try' and 'except' blocks to handle
expected runtime errors, specifically the ZeroDivisionError."""

def safe_division():
    """
    Prompts the user for two numbers and calculates their division,
    handling the ZeroDivisionError if the divisor is zero.
    """
    
    try:
        numerator = int(input("Enter the numerator (a): "))
        denominator = int(input("Enter the denominator (b): "))
        
        result = numerator / denominator
        print(f"\nResult of {numerator} / {denominator}: {result}")
        return result
        
    except ZeroDivisionError:
        print("\nERROR: denominator cannot be Zero. Division failed.")
        return None
        
    except ValueError:
        print("\nERROR: Invalid input. Please enter whole numbers only.")
        return None

safe_division()