def read_file_by_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        songs_list = []
        for line in lines:
            songs_list.append(line)

        songs_list.sort(key=str.lower)
        return songs_list

def write_file_by_lines(path, extra_text):
    with open(path, 'a', encoding='utf-8') as file:
        file.write(extra_text)

def main():
    songs_list = read_file_by_lines("songsInfo.txt")
    for song in songs_list:
        write_file_by_lines('newSongsFile.txt', song)
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Something goes wrong {e}")