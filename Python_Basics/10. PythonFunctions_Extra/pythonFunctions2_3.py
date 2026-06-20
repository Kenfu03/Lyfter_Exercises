text : str = str(input("Enter the text to check: "))

def vowels_in_text(text : str):
    vowels : str = "aAeEiIoOuU"
    result : int = 0
    for char in text:
        if char in vowels: result += 1
    return result

print(vowels_in_text(text))
    