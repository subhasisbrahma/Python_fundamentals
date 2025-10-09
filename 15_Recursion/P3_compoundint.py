"""Calculates the future value of an investment using compound interest 
through a recursive function, assuming a fixed 10% annual interest rate."""

# Define constants for clarity
ANNUAL_RATE_MULTIPLIER = 1.10 # Represents 1 + 0.10 (10% rate)

def calculate_compound_interest(principal, years):
    """
    Calculates the future value of a principal amount after a specified number of years.
    
    Parameters:
        principal (float): The initial investment amount (P).
        years (int): The duration of the investment (T).
        
    Returns:
        float: The final accumulated amount (Future Value).
    """
    
    # Error Handling: Ensure time is non-negative
    if years < 0:
        raise ValueError("Time (years) cannot be negative for this calculation.")

    # 1. Base Case (Time zero)
    if years == 0:
        return principal
    
    # 2. Recursive Step
    # Value at time T is the value at time (T-1) compounded for one more year.
    return calculate_compound_interest(principal, years - 1) * ANNUAL_RATE_MULTIPLIER

# Example usage
initial_principal = 2000
investment_years = 3

final_amount = calculate_compound_interest(initial_principal, investment_years)

print("--- Recursive Compound Interest Demo ---")
print(f"Principal: {initial_principal}")
print(f"Years: {investment_years}")

# The output is formatted to two decimal places for currency.
print(f"Final Amount (Future Value): {final_amount:.2f}")
