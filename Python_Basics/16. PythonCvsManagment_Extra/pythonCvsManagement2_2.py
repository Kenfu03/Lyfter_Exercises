from pythonCvsManagement2_1 import read_csv_into_dict, show_dict_information

class OutOfOptionsError(Exception):
    def __init__(self, option):
        super().__init__(f"No available option {option} in the list.")

def show_esrb():
    print("""Options to filter by ESRB:

E (Everyone): Suitable for all ages.
E10+ (Everyone 10+): Suitable for ages 10+.
T (Teen): Suitable for ages 13+.
M (Mature 17+): Suitable for ages 17+.
AO (Adults Only 18+): Suitable only for adults 18+.
RP (Rating Pending): Game not yet rated.\n""")


def ask_for_esrb():
    while True:
        try:
            esrb = str(input("Please enter the ESRB Classification to find: "))
            if esrb not in ["E", "E10+", "T", "M", "AO", "RP"]:
                raise OutOfOptionsError(esrb)
            return esrb
        except OutOfOptionsError as ex:
            print(ex)


def filter_games_by_esbr(esrb : str, games_dict : list[dict]):
    filter_games = []
    for game in games_dict:
        if game.get("ESRB") == esrb:
            filter_games.append(game)
    return filter_games


if __name__ == "__main__":
    try:
        show_esrb()
        esrb = ask_for_esrb()
        games_dict = read_csv_into_dict()
        filter_games = filter_games_by_esbr(esrb, games_dict)
        show_dict_information(filter_games, "ESRB " + esrb)
    except KeyboardInterrupt as e:
        print("Program kill by user.")


