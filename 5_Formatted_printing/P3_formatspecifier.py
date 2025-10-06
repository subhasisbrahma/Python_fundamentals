"""Demonstrate format specifiers and f-strings for cleaner output formatting."""

pi_value = 22 / 7

# 1. F-String (Recommended Method)
print(f"1. F-String (f''): Value of PI = {pi_value:.2f}")

# 2. .format() Method (Standard Method)
print('2. .format(): Value of PI = {0:.2f}'.format(pi_value))

# 3. String Modulo Operator (%) (Legacy Method)
print('3. Modulo (%%): Value of PI = %.2f' % (pi_value))
