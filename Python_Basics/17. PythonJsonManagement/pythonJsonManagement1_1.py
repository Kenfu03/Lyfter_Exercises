import json
PATH = "pokemons.json"


def read_json(file_path):
    with open(file_path, "r") as file:
        loaded_data = json.load(file)
    return loaded_data


def validate_number(str_input : str, is_float : bool):
    while True:
        try:
            if is_float:
                return float(input(str_input))
            else:
                return int(input(str_input))
        except ValueError:
            print("Please enter a number, not a word or text.")


def ask_held_item():
    if input("Please enter if the pokemon have held item y/n: ") == "y":
        return input("Held item name: ")
    else:
        return None


def ask_pokemon_skills():
    pokemon_skills : list[str] = []
    for skill in range(1, 5):
        pokemon_skills.append(input(f"Please enter the skill number {skill}: "))
    return pokemon_skills


def ask_pokemon_stats():
    pokemon_stats : dict[int]= {}
    stats : list[str] = ["hp", "attack", "defense", "sp_attack", "sp_defense", "speed"]
    for stat in stats:
        pokemon_stats[stat] = validate_number(f"Please enter the pokemon stat {stat} level: ", False)
    return pokemon_stats


def ask_pokemon():
    pokemon : dict = {}
    pokemon["name"] = input("Please enter the pokemon name: ")
    pokemon["type"] = input("Please enter the pokemon type: ")
    pokemon["level"] = validate_number("Please enter the pokemon level: ", False)
    pokemon["weight_kg"] = validate_number("Please enter the pokemon weight in kg: ", True)
    pokemon["is_shiny"] = True if input("Please enter is the pokemon is shiny y/n: ") == "y" else False
    pokemon["held_item"] = ask_held_item()
    pokemon["skills"] = ask_pokemon_skills()
    pokemon["stats"] = ask_pokemon_stats()
    return pokemon


def write_json(data_to_save):
    with open(PATH, "w") as file:
        json.dump(data_to_save, file, indent=4) 


if __name__ == "__main__":
    try:
        print("Welcome to pokemon system...")
        new_pokemon : dict = ask_pokemon()
        pokemon_list : list[dict] = read_json(PATH)
        pokemon_list.append(new_pokemon)
        write_json(pokemon_list)
        print(json.dumps(pokemon_list, indent=4))
    except KeyboardInterrupt as e:
        print("\nProgram kill by user.")
