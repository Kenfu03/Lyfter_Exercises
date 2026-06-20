import json
PATH = "../17. PythonJsonManagement1/pokemons.json"


def read_json():
    with open(PATH, "r") as file:
        loaded_data = json.load(file)
    return loaded_data


def show_pokemon_information(pokemon_list):
    for pokemon in pokemon_list:
        pokemon_name = pokemon.get("name")
        pokemon_type = pokemon.get("type")
        pokemon_level = pokemon.get("level")
        pokemon_weight = pokemon.get("weight_kg")
        pokemon_is_shiny = pokemon.get("is_shiny")
        if pokemon_is_shiny:
            print(f""" - Shiny {pokemon_name} of type {pokemon_type} 
weight {pokemon_weight}kg and is level {pokemon_level}""")
        else:
            print(f""" - {pokemon_name} of type {pokemon_type} 
weight {pokemon_weight}kg and is level {pokemon_level}""")


if __name__ == "__main__":
    try:
        pokemon_list = read_json()
        show_pokemon_information(pokemon_list)
    except KeyboardInterrupt as e:
        print("\nProgram kill by user.")
