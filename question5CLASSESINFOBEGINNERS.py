# Question 5
# Level 1

# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

import sys

class Employee:
    def __init__(self, first, last, pay): #the term self is convention, just the first thing that is skipped over, everything else is attributes 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}{last}@gmail.com"
    
    def fullname(self): #method, that does a function for every instance of the class (why it uses self)
        return self.first + self.last


emp1 = Employee("Cory","XKenshin",300000)
emp2 = Employee("Test","User",20000)

print(Employee.fullname(emp1)) #does the same thing, but calls it from the last, requiring the argument of the employee (or object)
print(emp1.fullname()) #doesnt look like an argument is given, but it is through the emp1, which gives it itself
# print('{} {}'.format(emp1.first, emp1.last)) #stupid way to do it without methods

class MethodMan:
    def __init__(self):
        self.s = "" #this is how u call a blank function, u need to have something in it that changes
    def getString(self):
        self.s = sys.stdin.readline().strip()
    def printString(self):
        print(self.s.upper())
stringthing = MethodMan()
stringthing.getString()
stringthing.printString()