import csv
import os

def set_games_len():
    games_dict = {}
    while True:
        try:
            games_len : int = int(input("How many games you want to add: "))
            return games_len
        except ValueError as e:
            print("Enter a valid number")


def ask_file_path():
    while True:
        file_path = str(input("Please enter the name of the file to add the information: ") + ".csv")
        option = input(f"The file you want to modify or create is '{file_path}'?, y/n: ")
        if option == "y":
            break
        else:
            continue
    return file_path


def create_games_dict(games_len : int):
    games_dict = []
    for i in range(1, games_len+1):
        game_dict = {}
        print(f"\n------- Enter information for the game number {i}---------")
        game_dict["Name"] = (input(f"Enter game name: "))
        game_dict["Genre"] = (input(f"Enter game genre: "))
        game_dict["Developer"] = (input(f"Enter game developer: "))
        game_dict["ESRB"] = (input(f"Enter game ESRB clasification: "))
        games_dict.append(game_dict)
    
    return games_dict


def save_csv(file_path, data):
    file_exists = os.path.exists(file_path)

    with open(file_path, 'a', encoding='utf-8', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')

        if not file_exists:
            writer.writeheader()

        writer.writerows(data)

def main():
    games_len = set_games_len()
    path = ask_file_path()
    games_dict = create_games_dict(games_len)
    save_csv(path, games_dict)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Something goes wrong {e}")
    except KeyboardInterrupt as e:
        print(f"Program finish by user.")