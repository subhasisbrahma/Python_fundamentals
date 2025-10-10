"""Demonstrates structured exception handling using 'try', multiple 'except' blocks,
and the 'finally' block."""

def safe_file_division_demo():
    """
    Prompts for input, performs division, handles multiple exceptions, 
    and demonstrates the 'finally' block's guarantee.
    """
    
    try:
        numerator = int(input("Enter numerator (a): "))
        divisor = int(input("Enter divisor (b): "))
        
        result = numerator / divisor
        print(f"Result: {result}")

        with open("race.txt", 'r') as file_handle:
            first_line = file_handle.readline().strip()
            print(f"File opened successfully. First line: '{first_line}'")

    except ZeroDivisionError:
        print("CAUGHT ERROR: Divisor cannot be Zero.")
        return None
        
    except FileNotFoundError:
        print("CAUGHT ERROR: Invalid file name (File not found).")
        return None

    except ValueError:
        print("CAUGHT ERROR: Invalid input type. Please enter whole numbers.")
        return None
        
    finally:
        print("--- FINALLY BLOCK EXECUTED ---")
        print("Mandatory cleanup/logging task completed.")
        
    return result

safe_file_division_demo()
