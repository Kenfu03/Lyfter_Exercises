import validators as val

def ask_input(prompt, validator):
    while True:
        try:
            value = input(prompt)
            return validator(value)
        except ValueError as e:
            print(e)


def ask_for_csv_path(prompt_part):
    return ask_input(f"Enter the csv file to {prompt_part} ", val.validate_csv_path)


def ask_option():
    return ask_input("Choose an option: ", val.validate_option)


def ask_name():
    return ask_input("Enter the student name ej: Kenneth Fuentes: ", val.validate_name)


def ask_section():
    return ask_input("Section: ", val.validate_section)


def ask_grade(subject : str):
    return ask_input(f"{subject} grade: ", val.validate_grade)


def ask_how_many_students():
    return ask_input("Please enter how many students you want to add: ", val.validate_int)