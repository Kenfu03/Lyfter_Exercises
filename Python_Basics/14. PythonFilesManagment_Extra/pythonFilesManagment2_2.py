def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        text : str = file.read()
        return text


def count_words_in_text(text : str):
    total_words = len(text.split())
    return total_words


def main():
    text = read_file("text.txt")
    print(f"This file have {count_words_in_text(text)} words")
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Something goes wrong {e}")