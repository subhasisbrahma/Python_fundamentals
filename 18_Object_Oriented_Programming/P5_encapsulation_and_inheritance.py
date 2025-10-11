"""Demonstrates encapsulation and inheritance combined in object-oriented programming."""

class Person:
    """Base Class: Demonstrates Encapsulation using private attributes."""
    def __init__(self, name, age): 
        self.name = name
        # Private Attribute: Python implements privacy via NAME MANGLING,
        # changing __age to _Person__age internally.
        self.__age = age 
    
    # Getter method: The professional way to access a private attribute.
    def get_age(self):
        return self.__age
    
    def display_basic_info(self):
        # We use the getter method here to access the age.
        print(f"Name: {self.name}, Age: {self.get_age()}", end="")

class Student(Person):
    """Derived Class: Inherits from Person and adds 'marks'."""
    def __init__(self, name, age, marks): 
        # Calls Person.__init__(name, age)
        super().__init__(name, age)
        self.marks = marks
    
    def display(self):
        # Prints parent info, then extends it with marks.
        super().display_basic_info()
        print(f", Marks: {self.marks}")

class Employee(Person):
    """Derived Class: Inherits from Person and adds 'salary'."""
    def __init__(self, name, age, salary): 
        super().__init__(name, age)
        self.salary = salary
    
    # FIX: Corrected method to display Employee data (removed self.marks).
    def display(self):
        # Accesses private age via the public get_age() method.
        print(f"Name: {self.name}, Age: {self.get_age()}, Salary: {self.salary}")


s = Student("Subhasis", 100, 150)
print("Student Info:")
s.display()
# Output: Name: Subhasis, Age: 100, Marks: 150

e = Employee("Brahma", 99, 100000)
print("Employee Info:")
e.display()
# Output: Name: Brahma, Age: 99, Salary: 100000