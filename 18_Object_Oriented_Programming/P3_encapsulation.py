"""Demonstrates encapsulation and use of private attributes in Python classes."""


class Student:
    """Represents a student and contains methods to manage their data."""
    
    # CONSTRUCTOR: Initializes unique attributes for each student object.
    def __init__(self, roll_no, name, marks): 
        # INSTANCE ATTRIBUTES (Data unique to this student)
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
    
    # METHOD: Displays the instance's unique data.
    def display_info(self):
        print(f"ID: {self.roll_no}, Name: {self.name}, Score: {self.marks}")

    # METHOD: Performs logic based on the instance's data.
    def evaluate_result(self):
        PASS_THRESHOLD = 120 # Define the threshold clearly
        
        if self.marks > PASS_THRESHOLD:
            print('Pass ✅')
        else:
            print('Fail ❌')


# S1: Object with passing data
s1 = Student(1, "Subhasis", 150)
s1.display_info()
s1.evaluate_result()
# Output:
# ID: 1, Name: Subhasis, Score: 150
# Pass

# S2: Object with failing data
s2 = Student(2, "Brahma", 100)
s2.display_info()
s2.evaluate_result()
# Output:
# ID: 2, Name: Brahma, Score: 100
# Fail