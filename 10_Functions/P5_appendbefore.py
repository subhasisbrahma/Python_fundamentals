"""Compares the manual (iterative) list concatenation logic with the highly efficient
Pythonic methods (using the '+' operator)."""

def list_appendbefore_manual(list_a, list_b):
    """
    Manual (Iterative) Approach: Concatenates list_b before list_a using loops and append().
    (Demonstrates the logic, but not the best practice.)
    """
    new_list = []
    
    # 1. Append all elements from the second list
    for element in list_b:
        new_list.append(element)
        
    # 2. Append all elements from the first list
    for element in list_a:
        new_list.append(element)
        
    return new_list

def list_appendbefore_pythonic(list_a, list_b):
    """
    Pythonic Approach: Concatenates list_b before list_a using the '+' operator.
    (This is the RECOMMENDED practice for its clarity and speed.)
    """
    return list_b + list_a

def demonstrate_concatenation():
    """
    Demonstrates manual vs Pythonic list concatenation methods.
    """
    list_to_append_after = [1, 2, 3, 4, 5]  # l
    list_to_append_before = [6, 7, 8, 9, 0] # z

    # 1. Manual/Original Method
    manual_result = list_appendbefore_manual(list_to_append_after, list_to_append_before)
    print("1. Manual Loop Result:", manual_result)
    
    # 2. Pythonic Method
    pythonic_result = list_appendbefore_pythonic(list_to_append_after, list_to_append_before)
    print("2. Pythonic (+) Result:", pythonic_result)
    
    # 3. Quickest Pythonic Method (Direct operator)
    quick_result = list_to_append_before + list_to_append_after
    print("3. Quick Operator Check:", quick_result)


# Execute demonstration
demonstrate_concatenation()
