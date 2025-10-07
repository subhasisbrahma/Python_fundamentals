"""Demonstrates common set operations."""

# 1. Relationship Tests (Subset and Superset)

set_small = {1, 3, 5}
set_large = {1, 2, 3, 4, 5}


# issubset(): Returns True if all elements of the first set are in the second set.
print(f"Is {set_small} a subset of {set_large}?: {set_small.issubset(set_large)}") 
# Output: True

# issuperset(): Returns True if the first set contains all elements of the second set.
print(f"Is {set_small} a superset of {set_large}?: {set_small.issuperset(set_large)}") 
# Output: False

# 2. Union (Combining Sets)

set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union combines all unique elements from both sets.
union_method = set_a.union(set_b)
union_operator = set_a | set_b  # Shortcut operator '|'

print(f"Union (Method/Operator): {union_method}, {union_operator}") 
# Output: {1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}

# 3. Intersection (Finding Common Elements)

# Intersection returns elements common to both sets.
intersection_method = set_a.intersection(set_b)
intersection_operator = set_a & set_b  # Shortcut operator '&'

print(f"Intersection (Method/Operator): {intersection_method}, {intersection_operator}") 
# Output: {3}, {3}


# 4. Difference (Elements in A but NOT B)

# Difference returns elements present in the first set but NOT in the second.
difference_method = set_a.difference(set_b)
difference_operator = set_a - set_b  # Shortcut operator '-'

print(f"Difference (Method/Operator): {difference_method}, {difference_operator}") 
# Output: {1, 2}, {1, 2}

# Note: B.difference(A) would yield {4, 5}.
