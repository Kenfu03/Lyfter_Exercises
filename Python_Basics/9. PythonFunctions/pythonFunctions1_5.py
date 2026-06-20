my_text:str = str(input("Please enter the text to check: "))

def uppercase_in_text(text:str):
    total:int = 0
    for letter in text:
        if letter.isupper():
            total += 1
    return total

def lowercase_in_text(text:str):
    total:int = 0
    for letter in text:
        if letter.islower():
            total += 1
    return total



print(f"There's {uppercase_in_text(my_text)} upper cases and {lowercase_in_text(my_text)} lower cases")
