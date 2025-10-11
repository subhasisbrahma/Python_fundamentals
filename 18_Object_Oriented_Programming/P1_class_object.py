"""Demonstrates basic class and object creation in Python."""

class Student:
    # 1. Class Attribute: Shared by ALL students
    school_name = "RVN"

    # 2. Constructor: Initializes a new student object with unique data
    # Note: 'self' refers to the object being created (s1, s2, etc.)
    def __init__(self, roll_no, name):
        self.roll_no = roll_no # Instance Attribute
        self.name = name       # Instance Attribute

    # 3. Simple Method: Accesses the instance's own data
    @staticmethod
    def print_info(student_object):
        print(f"Roll No: {student_object.roll_no}, Name: {student_object.name}, School: {Student.school_name}")



# S1: Object is created, __init__ runs, setting roll_no=1 and name="Subhasis"
s1 = Student(roll_no=1, name="Subhasis")
Student.print_info(s1)
# Output: Roll No: 1, Name: Subhasis, School: RVN

# S2: Object created. roll_no=2 and name="Alice" are set by __init__.
s2 = Student(roll_no=2, name="Xyz") 
Student.print_info(s2)
# Output: Roll No: 2, Name: Xyz , School: RVN

# S3: Create an object, then directly modify its instance attribute.
s3 = Student(roll_no=50, name="Brahma")
s3.roll_no = 51 # Direct modification of an instance attribute
Student.print_info(s3)
# Output: Roll No: 51, Name: Brahma, School: RVN