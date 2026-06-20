def ask_for_text():
    text : str = str(input("Please enter the text to add: "))
    name_of_file : str = str(input("Please enter the name of the file: "))
    return (text, name_of_file)


def create_file(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)

def add_to_file(path, text):
    with open(path, 'a', encoding='utf-8') as file:
        file.write("\n" + text)


def main():
    text, path = ask_for_text()
    try:
        with open(path, "r") as file:
            content = file.read()
            print("The file exists! Content successfully added.")
            return add_to_file(path, text)
    
    except FileNotFoundError:
        print("The file does not exist. Content successfully created.")
        return create_file(path, text)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Something goes wrong {e}")