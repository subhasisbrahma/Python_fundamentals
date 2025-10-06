"""Show different printing styles and string formatting methods in Python."""

base_number = int(input("Enter the number: "))

print()
print("--- Multiplication Table for", base_number, "(Showing 4 Formats) ---")

for multiplier in range(1, 11):
    product = base_number * multiplier

    # 1. Normal Way (Comma Separation)
    print("1. Normal Print:", base_number, "X", multiplier, "=", product)

    # 2. F-String (Modern)
    print(f"2. F-String:     {base_number} X {multiplier} = {product}")

    # 3. Format Function
    print("3. .format():    {0} X {1} = {2}".format(base_number, multiplier, product))

    # 4. String Modulo Operator (%)
    print("4. Modulo (%): %d X %d = %d" % (base_number, multiplier, product))

    print("-" * 30)
