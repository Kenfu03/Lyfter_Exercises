from pythonCvsManagement2_1 import read_csv_into_dict

def find_games_per_developer(games_dict : list[dict], developer_name : str):
    games_per_developer : list[dict] = []
    for game in games_dict:
        if game.get("Developer") == developer_name:
            games_per_developer.append(game)
    return games_per_developer


def show_developer_information(games_dict : list[dict], developer_name : str):
    print(f"Games developed by {developer_name}...")
    for game in games_dict:
        print(f"- {game.get("Name")} (Classification: {game.get("ESRB")}, Genre: {game.get("Genre")})")


if __name__ == "__main__":
    games_dict : list[dict] = read_csv_into_dict()
    developer_name : str = input("Please enter the developer name to find: ")
    filter_games : list[dict] = find_games_per_developer(games_dict, developer_name)
    show_developer_information(filter_games, developer_name)