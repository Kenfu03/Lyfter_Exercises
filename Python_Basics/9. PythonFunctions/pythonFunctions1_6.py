my_words:str = str(input("Please enter all words to be sorted alphabetically, separating them with -: "))

def string_to_list(text: str):
    return text.split("-")

def sort_words_in_list(list:list[str]):
    return sorted(list, key=str.lower)


def list_to_string(words:list[str]):
    return "-".join(words)


list = string_to_list(my_words)
final_result = list_to_string(sort_words_in_list(list))
print(f"{my_words} Sorted alphabetically > {final_result}")