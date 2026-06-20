list_len : int = int(input("Enter how many words you want to check: "))

def list_creation(list_size:int):
    words : str = []
    
    for i in range (1, list_size+1):
        word : str = str(input(f"Enter the word {i}: "))
        words.append(word)

    return words

my_list : list[str] = list_creation(list_len)
min_letters : int = int(input("Enter the minimun size in a word: "))

def check_minimun_size(words:list[str], n:int):
    final_list : list[str] = []
    for word in words:
        if len(word) > n: final_list.append(word)
    return final_list

print(check_minimun_size(my_list,min_letters))
