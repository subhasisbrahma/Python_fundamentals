"""Demonstrate basic calendar operations such as displaying months"""

# Method 1: Standard Import (Best Practice)
import calendar
# To call a function, you must prefix it with the module name (e.g., calendar.month).
print(calendar.month(2005, 1))
# Output is a formatted calendar for January 2005.
# Prints the full year calendar
print(calendar.calendar(2002))
# Output is a formatted calendar for the entire year 2002.


# Method 2: Wildcard Import (Use with Caution)
# This imports ALL names (functions, variables) directly into the current namespace.
# It makes functions callable without the 'calendar.' prefix, but can lead to
# naming conflicts if you import multiple modules this way.
from calendar import *
# The 'calendar' function is now callable directly.
print(calendar(2005))
# Output is a formatted calendar for the entire year 2005.


# Method 3: Aliased Import (For Specific Functions)
# This imports a specific function and assigns it a shorter, custom name.
from calendar import month as get_month
# The function is called using the alias 'get_month'.
print(get_month(2024, 8))
# Output is a formatted calendar for August 2024.
