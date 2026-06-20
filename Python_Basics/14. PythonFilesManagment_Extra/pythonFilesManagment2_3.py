def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        text_list : str = file.readlines()
        return text_list


def lowercase_to_uppercase(text_list : list[str]):
    new_text_list : list[str] = []
    for line in text_list:
        new_text_list.append(line.upper())
    return new_text_list


def write_file_per_line(path : str, text_list : list[str]):
    with open(path, 'w', encoding='utf-8') as file:
        file.writelines(text_list)


def main():
    text_list = read_file("text.txt")
    write_file_per_line("text_in_uppercase.txt", lowercase_to_uppercase(text_list))
    print(read_file("text_in_uppercase.txt"))
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Something goes wrong {e}")