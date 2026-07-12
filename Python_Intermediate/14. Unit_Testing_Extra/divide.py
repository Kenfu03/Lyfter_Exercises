def divide_validate_data(func):
    def wrapper(n1, n2):
        if not isinstance(n1, (int, float)) or not isinstance(n2, (int, float)):
            raise TypeError("Must be numbers")
        if n2 == 0:
            raise ValueError("You cannot divide by zero.")
        return func(n1, n2)
    return wrapper


@divide_validate_data
def divide(number1, number2):
    return number1 / number2
