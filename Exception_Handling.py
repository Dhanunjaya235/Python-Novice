# EXCEPTION HANDLING IN PYTHON

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")
    

# Exception Chaining

def function_a():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        raise ValueError("Invalid input") from e
    else:
        print("Result:", result)

def function_b():
    try:
        function_a()
    except ValueError as e:
        print(f"Caught an error: {e}")
        print(f"Original error: {e.__cause__}")

function_b()

# Custom Exception
class NegativeNumberError(Exception):
    pass

def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(e)
