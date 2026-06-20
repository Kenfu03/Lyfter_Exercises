def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        text : str = file.read()
        return text


def remove_line_break(text : str):
    return text.replace("\n", " ")


def write_file(path : str, text : str):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)


def main():
    text = read_file("text.txt")
    new_text = remove_line_break(text)
    write_file("text_without_line_breaks.txt", new_text)
    print(read_file("text_without_line_breaks.txt"))
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Something goes wrong {e}")