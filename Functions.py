# FUNCTIONS IN PYTHON

# 1. Basic Function
def greet():
    print("Hello, World!")

greet()

# 2. Function with Parameters
def add(a, b):
    return a + b

print("Sum:", add(3, 4))

# 3. Function with Default Arguments
def power(base, exponent=2):
    return base ** exponent

print("Power:", power(3))
print("Power with exponent:", power(3, 3))

# 4. Function with Variable Arguments (*args)
def sum_all(*args):
    return sum(args)

print("Sum of all:", sum_all(1, 2, 3, 4, 5))

# 5. Function with Keyword Arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")

# 6. Function Returning Multiple Values
def operations(a, b):
    return a + b, a - b, a * b, a / b

sum_res, diff_res, prod_res, div_res = operations(10, 2)
print("Results:", sum_res, diff_res, prod_res, div_res)

# 7. Recursive Function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))

# 8. Lambda Function
square = lambda x: x * x
print("Lambda Square:", square(5))

# 9. Function with Map
def square_num(x):
    return x * x

numbers = [1, 2, 3, 4]
squared_numbers = list(map(square_num, numbers))
print("Mapped Squares:", squared_numbers)

# 10. Function with Filter
def is_even(n):
    return n % 2 == 0

even_numbers = list(filter(is_even, numbers))
print("Filtered Evens:", even_numbers)

# 11. Function with Reduce
from functools import reduce, wraps
def multiply(x, y):
    return x * y

product = reduce(multiply, numbers)
print("Reduced Product:", product)

# 12. Nested Functions
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
print("Closure Result:", closure(5))

# 13. Function with Nonlocal Variable
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

incrementer = counter()
print("Counter:", incrementer())
print("Counter:", incrementer())

# 14. Function with Global Variable
global_var = 100
def modify_global():
    global global_var
    global_var += 10
modify_global()
print("Global Variable:", global_var)

# 15. Function Decorators
def decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function execution")
        print("After function execution")
        func()
    wrapper.__name__ = func.__name__
    return wrapper

@decorator
def say_hello():
    print("Hello!, Decorator")

say_hello()

# 16. Generator Function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print("Countdown:", num)

# 17. Function with Iterator Class
class CustomRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

for num in CustomRange(1, 5):
    print("Custom Range:", num)

# 18. Function Aliasing
def greet_person(name):
    return f"Hello, {name}!"

greet_alias = greet_person
print(greet_alias("Bob"))

# 19. Function Annotations
def multiply_annotated(a: int, b: int) -> int:
    return a * b

print("Annotated Multiplication:", multiply_annotated(4, 5))

# 20. Function with Try-Except
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print("Safe Division:", safe_divide(10, 0))
