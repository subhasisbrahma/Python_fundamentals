"""Demonstrates the use of the 'raise' keyword to enforce a condition (age limit) 
and signal an error."""

# Define the eligibility rule as a constant
MINIMUM_AGE = 18

def check_age_eligibility():
    """
    Prompts the user for age and raises a custom exception if the user is underage.
    
    Returns:
        int: The age if it meets the minimum requirement.
        
    Raises:
        Exception: If the entered age is below MINIMUM_AGE.
    """
    age = int(input(f"Enter your age (Must be {MINIMUM_AGE} or older): "))
    
    # Core Logic: If the condition is not met, explicitly stop execution and raise an error.
    if age < MINIMUM_AGE:
        # The 'raise' keyword creates and throws a custom exception with a message.
        raise Exception("You are underage")
        
    return age

check_age_eligibility()
