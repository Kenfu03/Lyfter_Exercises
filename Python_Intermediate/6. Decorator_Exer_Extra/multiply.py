from datetime import datetime
from functools import wraps


def log_call(func):
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        now = datetime.now()
        print(f"func: {func.__name__} - args: {', '.join(str(a) for a in args)} [{now}] - Result: {result}")
        return result

    return wrapper


def validate_numbers(func):
    @wraps(func)
    def wrapper(*args):
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise ValueError("All arguments must be numbers.")

        return func(*args)

    return wrapper


@log_call
@validate_numbers
def multiply(num1, num2):
    return num1 * num2


try:
    #result = multiply("hola", 5)
    result = multiply(4, 5)
    print(f"Result: {result}")
except ValueError as e:
    print(e)