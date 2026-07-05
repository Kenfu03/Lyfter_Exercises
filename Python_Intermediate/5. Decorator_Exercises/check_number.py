def check_numbers(func):
    def wrapper(*args):
        if not all(isinstance(arg, (int, float)) for arg in args):
            raise ValueError("All arguments must be numbers.")

        return func(*args)

    return wrapper


@check_numbers
def random_function(*args):
    return sum(args) / len(args)

try:
    print(random_function(1, "Hola", 67, 54, 34, 22, 57, 75, 755, 4, 65))
except ValueError as e:
    print(e)