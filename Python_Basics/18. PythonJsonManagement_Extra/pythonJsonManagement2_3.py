import json
PATH = "../17. PythonJsonManagement/pokemons.json"


def read_json():
    with open(PATH, "r") as file:
        loaded_data = json.load(file)
    return loaded_data


def show_pokemon_stats(pokemon_list):
    translate_keys = ["Nombre", "Ataque", "Defensa", 
    "Velocidad", "Ataque especial", "Defensa especial"]
    keys_to_find = ["name", "attack", "defense", "speed", 
    "sp_attack", "sp_defense"]
    for pokemon in pokemon_list:
        print(f"{translate_keys[0]}: {pokemon.get(keys_to_find[0])}")
        pokemon_stats = pokemon.get("stats")
        for i in range(1, len(keys_to_find)):
            print(f"{translate_keys[i]}: {pokemon_stats.get(keys_to_find[i])}")
        print("-------------------------")


if __name__ == "__main__":
    try:
        pokemon_list = read_json()
        show_pokemon_stats(pokemon_list)
    except KeyboardInterrupt as e:
        print("\nProgram kill by user.")
