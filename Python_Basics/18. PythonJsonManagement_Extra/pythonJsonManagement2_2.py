import json
PATH = "../17. PythonJsonManagement1/pokemons.json"


def read_json():
    with open(PATH, "r") as file:
        loaded_data = json.load(file)
    return loaded_data


def find_pokemon_by_name(pokemon_list : list[dict], type_to_find : str):
    pokemon_names : list[str] = []
    for pokemon in pokemon_list:
        pokemon_type : str = pokemon.get("type")
        pokemon_name : str = pokemon.get("name")
        if pokemon_type == type_to_find:
            pokemon_names.append(pokemon_name)
    return pokemon_names


if __name__ == "__main__":
    try:
        type_to_find = input("Please enter the pokemon type to find (Fire, Water, Plant, etc): ")
        pokemon_names = find_pokemon_by_name(read_json(), type_to_find)
        print(f"The pokemons with type '{type_to_find}' are...")
        for pokemon in pokemon_names:
            print(pokemon)
    except KeyboardInterrupt as e:
        print("\nProgram kill by user.")
    

