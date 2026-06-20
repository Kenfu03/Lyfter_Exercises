my_list = ['4', 'hola', '10', '5.2']

def convert_to_int(string_list : list[str]):
    for string in string_list:
        try:
            number : int = int(string)
            print(f"'{string}' converted to {number}")
        except ValueError:
            print(f"Impossible to convert '{string}'")

def main():
    print("Result: ")
    convert_to_int(my_list)

if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(f"Something goes wrong: {ex}")