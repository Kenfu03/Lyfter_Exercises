from pythonCvsManagement2_1 import read_csv_into_dict

def genre_count(games_dict : list[dict]):
    genre_dict = {}
    for game in games_dict:
        game_genre = game.get("Genre")
        if genre_dict.get(game_genre) == None:
            genre_dict[game_genre] = 1
        else:
            genre_dict[game_genre] += 1
    return dict(sorted(genre_dict.items()))

if __name__ == "__main__":
    games_dict = read_csv_into_dict()
    genre_count = genre_count(games_dict)
    print("Genres founded...")
    for keys, values in genre_count.items():
        print(f"{keys}: {values}")