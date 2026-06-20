text:str = str(input("Please enter the text to check: "))
character_to_find:str = str(input("Please enter the character to find in the text: "))

def find_character_in_text(text:str, character:str):
    result:int = 0
    for char in text:
        if char == character: result += 1
    return result

print(f"The character {character_to_find} appears {find_character_in_text(text, character_to_find)} times")