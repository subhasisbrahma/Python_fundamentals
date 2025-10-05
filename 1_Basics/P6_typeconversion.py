"""Demonstrates type conversion (casting) between integers, floats, and strings in Python."""

# TYPE CASTING
# Converting to Integer (int)

# Float to Integer: int() truncates the decimal part, it does NOT round.
int_from_float = int(7.8)
# String to Integer: The string must contain only digits.
int_from_string = int("15")

print(int_from_float, type(int_from_float))    # Output: 7 <class 'int'>
print(int_from_string, type(int_from_string))  # Output: 15 <class 'int'>


# Converting to Float (float)

# Integer to Float: Adds a .0 to the number.
float_from_int = float(7)
# String to Float: Converts a string containing a whole number or a decimal.
float_from_string_whole = float("15")
float_from_string_decimal = float("15.0")

print(float_from_int, type(float_from_int))           # Output: 7.0 <class 'float'>
print(float_from_string_whole, type(float_from_string_whole))  # Output: 15.0 <class 'float'>
print(float_from_string_decimal, type(float_from_string_decimal))# Output: 15.0 <class 'float'>


# Converting to String (str)

# int/float to String: Converts the numeric value into a sequence of characters.
str_from_int = str(15)
str_from_float = str(7.8)

print(str_from_int, type(str_from_int))   # Output: 15 <class 'str'>
print(str_from_float, type(str_from_float))  # Output: 7.8 <class 'str'>


# Converting to Boolean (bool)
# Rule: Only "empty" values evaluate to False. Everything else is True.
# The "empty" values are: 0, 0.0, None, "", [], {}, ().

# Numeric conversions (non-zero is True)
bool_from_positive_int = bool(15)   # Non-zero integer
bool_from_zero_int = bool(0)        # Zero is the ONLY integer that is False
bool_from_negative_int = bool(-15)  # Negative numbers are also True
bool_from_positive_float = bool(22.0)
bool_from_zero_float = bool(0.0)    # Zero float is False
bool_from_negative_float = bool(-22.0)

# String conversions (non-empty string is True)
bool_from_non_empty_string_digits = bool("11")
bool_from_non_empty_string_zero = bool("0")
bool_from_empty_string = bool("")       # The ONLY string that is False
bool_from_non_empty_string_text = bool("Subhasis")

print(bool_from_positive_int, type(bool_from_positive_int))     # Output: True <class 'bool'>
print(bool_from_zero_int, type(bool_from_zero_int))            # Output: False <class 'bool'>
print(bool_from_negative_int, type(bool_from_negative_int))    # Output: True <class 'bool'>
print(bool_from_positive_float, type(bool_from_positive_float))# Output: True <class 'bool'>
print(bool_from_zero_float, type(bool_from_zero_float))        # Output: False <class 'bool'>
print(bool_from_negative_float, type(bool_from_negative_float))# Output: True <class 'bool'>
print(bool_from_non_empty_string_digits, type(bool_from_non_empty_string_digits))# Output: True <class 'bool'>
print(bool_from_non_empty_string_zero, type(bool_from_non_empty_string_zero))  # Output: True <class 'bool'>
print(bool_from_empty_string, type(bool_from_empty_string))      # Output: False <class 'bool'>
print(bool_from_non_empty_string_text, type(bool_from_non_empty_string_text)) # Output: True <class 'bool'>