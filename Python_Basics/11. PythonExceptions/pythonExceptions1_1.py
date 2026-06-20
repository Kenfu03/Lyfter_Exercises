print("Welcome to in-command calculator")

class OutOfOptionsError(Exception):
    def __init__(self, operation : int):
        super().__init__(f"No available option {operation} in the list.")

def get_number(text: str):
    while True:
        try:
            return float(input(f"Please enter the {text} number: "))
        except ValueError:
            print("Please enter a number, not a word or text.")


def print_options(number : float):
    print(f"""Here you have the options to do with your actual number {number}
    1. Add
    2. Subtract
    3. Multiplication
    4. Division
    5. Clear result
    6. Exit""")


def get_operation():
    while True:
        try:
            operation = int(input("Please enter the option number: "))

            if operation not in [1, 2, 3, 4, 5, 6]:
                raise OutOfOptionsError(operation)

            return operation

        except ValueError:
            print("Please enter a number, not a word or text.")

        except OutOfOptionsError as ex:
            print(ex)


def calculator(first_number : float, second_number : float, operation : int):
    match (operation):
        case (1):
            return ("+", first_number + second_number)
        case (2):
            return ("-", first_number - second_number)
        case (3):
            return ("x", first_number * second_number)
        case (4):
            return ("/", first_number / second_number)


def main():
    first_number = get_number("first")
    while True:
        print_options(first_number)
        operation = get_operation()
        if operation == 6:
            print("Thanks for using this calculator, bye")
            break
        if operation == 5:
            print(f"Number {first_number} erased")
            first_number = get_number("first")
            continue
        second_number = get_number("second")
        try:
            if operation == 4 and second_number == 0:
                raise ZeroDivisionError
            symbol, result = calculator(
                first_number,
                second_number,
                operation
            )
            print(
                f"{first_number} {symbol} {second_number} = {result}"
            )
            first_number = result
        except ZeroDivisionError:
            print("Impossible to divide by zero")

if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(f"Something goes wrong: {ex}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")