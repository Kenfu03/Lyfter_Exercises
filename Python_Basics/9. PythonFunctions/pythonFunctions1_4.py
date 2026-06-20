word = str(input("Please enter the word to reverse: "))

def reversed_word(word:str):
    reversed_word = ""
    for i in range(len(word)-1, -1, -1):
        reversed_word += word[i]
    return reversed_word

print(reversed_word(word))