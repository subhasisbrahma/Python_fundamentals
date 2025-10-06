"""Compute profit or loss based on cost price and selling price."""

while True:
    # Get Employee ID (Outer Loop Control)
    employee_id = input("Enter the Employee Id (or enter -1 to quit): ")
    
    if employee_id == "-1":
        print()
        print("Program terminated. Goodbye!")
        break  # Exit outer loop

    total_pnl = 0
    print()

    # Get first trade amount
    trade_amount = int(input("Enter the trade amount (or 0 to finalize): "))

    # Inner loop: sum trades until 0 is entered
    while trade_amount != 0:
        total_pnl += trade_amount
        trade_amount = int(input("Enter the trade amount (or 0 to finalize): "))

    # Output final result for the employee
    print()
    print(">>>> FINAL RESULT: PnL for Employee", employee_id, "is", total_pnl)
