
def ask_name():
    while True:
        name : str = input("Please enter your name: ")
        if validate_name(name):
            break
    return name


def validate_name(name : str):
    try:
        if not all(char.isalpha() or char == " " for char in name):
            raise ValueError
        else:
            return True
    except ValueError as e:
        print("The number cannot be a number!")


def ask_age():
    while True:
        try:
            return int(input(f"Please enter your age: "))
        except ValueError:
            print("Please enter a number, not a word or text.")

def main():
    print(f"Hello {ask_name()} your age is {ask_age()}")

if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(f"Something goes wrong: {ex}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
