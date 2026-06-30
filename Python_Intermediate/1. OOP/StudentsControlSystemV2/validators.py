def validate_csv_path(file_name):
    if not all(char.isalpha() or char == "." for char in file_name):
        raise ValueError("No empty spaces please")
    if file_name[-4:] != ".csv":
        raise ValueError("The path need to have the .csv")
    if not input(f"You want to work with '{file_name}' y/n: ") == "y":
        raise ValueError("Please add the cvs file name")
    return file_name


def validate_option(option):
    try:
        number = int(option)
    except ValueError:
        raise ValueError("The program only accept numbers for options")

    if number not in range(1,10):
        raise ValueError("Please choose an option between 1 and 9")

    return number


def validate_only_letters(value : str) -> bool:
    return not all(char.isalpha() or char == " " for char in value)


def validate_name(name: str) -> str:
    if not name:
        raise ValueError("Name cannot be empty.")

    if len(name.split()) > 2 or len(name.split()) < 2:
        raise ValueError("Need to be name and lastname. ej: 'Kenneth Fuentes'")

    if validate_only_letters(name):
        raise ValueError("Name must contain only letters.")

    return name


def validate_section(value: str) -> str:
    value = value.strip().upper()

    if len(value) not in (2, 3):
        raise ValueError("Section must have the format 1A or 12B.")

    number = value[:-1]
    group = value[-1]

    try:
        number = int(value[:-1])
    except ValueError:
        raise ValueError("Section must have the format 1A or 12B.")

    if not 1 <= number <= 12:
        raise ValueError("Section number must be between 1 and 12.")

    if group not in ("A", "B", "C", "D"):
        raise ValueError("Section must be A, B, C or D.")

    return f"{number:02d}{group}"


def validate_grade(value : str) -> float:
    try:
        float_value : float = float(value)
    except ValueError:
        raise ValueError("Please enter a valid number.")

    if float_value < 0 or float_value > 100:
        raise ValueError("Please enter a grade between 0 and 100")

    return float_value


def validate_int(value):
    try:
        number = int(value)
    except ValueError:
        raise ValueError("Please enter a valid number")
    return number