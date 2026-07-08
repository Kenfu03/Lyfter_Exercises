def reversed_word(word:str):
    reversed_word = ""
    for i in range(len(word)-1, -1, -1):
        reversed_word += word[i]
    return reversed_word



if __name__ == "__main__":
    try:
        word = str(input("Please enter the word to reverse: "))
        print(reversed_word(word))
    except ValueError as e:
        print(e)