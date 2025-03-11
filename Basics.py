"""
Python Basics and Syntax Overview
This script covers fundamental Python concepts including variables, data types, operators, control flow, functions, lists, tuples, dictionaries, sets, classes, and file handling.
"""

# 1. Variables & Data Types
x = 10  # Integer
y = 3.14  # Float
name = "John"  # String
is_valid = True  # Boolean

# Type Checking
print(type(x), type(y), type(name), type(is_valid))

# 2. Operators
# Arithmetic Operators
a, b = 10, 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

# Comparison & Logical Operators
print(a > b, a < b, a == b, a != b)
print(True and False, True or False, not True)

# 3. Control Flow
num = 10
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Loops
for i in range(5):
    print(i)

x = 0
while x < 5:
    print(x)
    x += 1

# 4. Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Lambda Function
square = lambda x: x * x
print(square(5))

# 5. Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
fruits.remove("banana")
print(fruits)

# List Comprehension
squares = [x**2 for x in range(5)]
print(squares)

# 6. Tuples (Immutable List)
coordinates = (10, 20)
print(coordinates[0])

# 7. Dictionaries
person = {"name": "Alice", "age": 25}
person["city"] = "New York"
print(person)

# 8. Sets (Unique Values)
numbers = {1, 2, 3, 3, 2}
numbers.add(4)
print(numbers)

# 9. Classes & Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}."

p1 = Person("Alice", 25)
print(p1.greet())

# 10. File Handling
with open("test.txt", "w") as file:
    file.write("Hello, World!")

with open("test.txt", "r") as file:
    print(file.read())
