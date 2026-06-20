import csv

def read_csv_into_dict():
    with open('../15. PythonCvsManagment1/games.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        games = list(reader)
    return games


def show_dict_information(games_dict : list[dict], title):
    keys_translation = {
        "Name": "Nombre", 
        "Genre": "Genero", 
        "Developer": "Desarrollador", 
        "ESRB": "Clasificacion"}
    print(f"_________{title}_________")
    for game in games_dict:
        print("_________________________")
        for keys, values in game.items():
            print(f"{keys_translation.get(keys)}: {values}")


if __name__ == "__main__":
    games_dict = read_csv_into_dict()
    show_dict_information(games_dict, "Games")