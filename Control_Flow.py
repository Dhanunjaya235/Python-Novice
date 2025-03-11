# Control Flow in Python

# Conditional Statements
x = 10
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

# Nested If
if x < y:
    if x % 2 == 0:
        print("x is even and less than y")
    else:
        print("x is odd and less than y")

# Ternary Conditional Operator
max_value = x if x > y else y
print("Max value:", max_value)

# For Loop
for i in range(5):
    print("Iteration:", i)

# While Loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Break and Continue
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print("Odd number:", i)

# Else with Loop
for i in range(3):
    print("Loop iteration:", i)
else:
    print("Loop completed without break")

# Try-Except-Finally
try:
    num = int("xyz")
except ValueError as e:
    print("Error:", e)
finally:
    print("Execution completed")

# Raising Exceptions
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

try:
    print(divide(10, 0))
except ZeroDivisionError as e:
    print("Caught error:", e)

# Match-Case (Python 3.10+)
def check_status(code):
    match code:
        case 200:
            print("OK")
        case 400:
            print("Bad Request")
        case 404:
            print("Not Found")
        case _:
            print("Unknown status")

check_status(200)
check_status(500)

# List Comprehension with If Condition
squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares:", squares)

# Dictionary Comprehension
num_dict = {x: x**2 for x in range(5)}
print("Dictionary:", num_dict)

# Nested Loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Using Pass (Placeholder for Future Code)
def future_function():
    pass

# Infinite Loop (with Break Condition)
i = 0
while True:
    if i >= 3:
        break
    print("Infinite Loop Iteration:", i)
    i += 1

# Checking Membership in List
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list")

# Using All and Any
values = [True, False, True]
print("All True?", all(values))
print("Any True?", any(values))

# Using Enumerate
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(index, name)

# Using Zip
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
for num, letter in zip(list1, list2):
    print(num, letter)

# Looping Over Dictionary
info = {"name": "Alice", "age": 25}
for key, value in info.items():
    print(key, ":", value)

# Custom Iterator
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

for num in Counter(1, 3):
    print("Counter:", num)

# Recursion with Control Flow
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
