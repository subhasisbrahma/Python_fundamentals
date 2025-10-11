"""Demonstrates core object-oriented programming concepts in Python."""

class Student:
    # 1. CLASS ATTRIBUTE: Shared counter across ALL Student objects
    student_count = 0 
    
    # 2. CONSTRUCTOR METHOD: Initializes unique data for a new object
    def __init__(self, roll_no, name): 
        # INSTANCE ATTRIBUTES (Unique to s1, s2, etc.)
        self.roll_no = roll_no
        self.name = name
    
    # 3. INSTANCE METHOD: Operates on the current object's unique data
    def display_info(self): 
        print(f"Roll No: {self.roll_no}, Name: {self.name}")


# S1: Object created. The instance attributes (roll_no, name) are set.
s1 = Student(1, "Subhasis")
Student.student_count += 1 # Update the shared class attribute
s1.display_info()
# Output: Roll No: 1 Subhasis

# S2: Another object created, with its own unique roll_no and name.
s2 = Student(2, "Brahma")
Student.student_count += 1 # Update the shared class attribute again
s2.display_info()
# Output: Roll No: 2 Brahma

# Access the final, shared state of the class attribute
print(f"Total Students Registered: {Student.student_count}")
# Output: 2