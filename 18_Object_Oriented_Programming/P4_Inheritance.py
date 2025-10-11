"""Demonstrates inheritance in object-oriented programming."""

class Person:
    """Base Class: Holds common attributes (name, age)."""
    def __init__(self, name, age): 
        # Instance Attributes shared by all subclasses
        self.name = name
        self.age = age
    
    def display(self):
        """Method to display basic Person info."""
        print(f"Name: {self.name}, Age: {self.age}", end="")

class Student(Person):
    """Derived Class: Inherits from Person and adds 'marks'."""
    def __init__(self, name, age, marks): 
        # Call the parent's constructor to handle 'name' and 'age' initialization
        super().__init__(name, age) 
        # Initialize the unique attribute
        self.marks = marks
    
    # Method Overriding (Extending Parent's Method)
    def display(self):
        # Call the parent's display method first (prints name, age)
        super().display()
        # Then print the unique attribute
        print(f", Marks: {self.marks}")

class Employee(Person):
    """Derived Class: Inherits from Person and adds 'salary'."""
    def __init__(self, name, age, salary): 
        super().__init__(name, age)
        self.salary = salary
    
    # Method Overriding (Replacing Parent's Method)
    def display(self):
        # This method completely replaces the parent's version.
        print(f"Employee Info: {self.name}, Age: {self.age}, Salary: {self.salary}")


# Student object: Inherits name/age, adds marks
s = Student("Subhasis", 100, 150)
print("Student Info (Extending Parent's Method):")
s.display()
# Output: Name: Subhasis, Age: 100, Marks: 150


# Employee object: Inherits name/age, adds salary
e = Employee("Brahma", 99, 100000 )
print("Employee Info (Overriding Parent's Method):")
e.display()
# Output: Employee Info: Brahma, Age: 99, Salary: 100000