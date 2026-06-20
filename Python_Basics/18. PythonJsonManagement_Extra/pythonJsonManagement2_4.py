import json
PATH = "../17. PythonJsonManagement1/pokemons.json"


def read_json():
    with open(PATH, "r") as file:
        loaded_data = json.load(file)
    return loaded_data


def group_by_type(pokemon_list : list[dict]):
    pokemon_type_dict = {}
    for pokemon in pokemon_list:
        pokemon_type : str = pokemon.get("type")
        if pokemon_type_dict.get(pokemon_type):
            pokemon_type_dict.get(pokemon_type).append(pokemon)
        else:
            pokemon_type_dict[pokemon_type] = [pokemon]
    return pokemon_type_dict


def average_level_per_type(pokemon_type_dict):
    average_type_level = {}
    for pokemon_type, pokemons in pokemon_type_dict.items():
        level_sum = 0
        for pokemon in pokemons:
            level_sum += pokemon.get("level")
        average = level_sum / len(pokemons)
        average_type_level[pokemon_type] = average
    return average_type_level


if __name__ == "__main__":
    try:
        pokemon_list = read_json()
        pokemon_type_list = group_by_type(pokemon_list)
        average_type_level = average_level_per_type(pokemon_type_list)
        for keys, values in average_type_level.items():
            print(f"Tipo: {keys} -> Promedio de nivel: {values}")
    except KeyboardInterrupt as e:
        print("\nProgram kill by user.")