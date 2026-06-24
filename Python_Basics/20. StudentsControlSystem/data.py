import csv
import os

def read_txt_file():
    with open("csv_path.txt", 'r', encoding='utf-8') as file:
        cvs_file_name = file.read()

        return cvs_file_name


def write_txt_file(cvs_file_path):
    with open("csv_path.txt", 'w', encoding='utf-8') as file:
        file.write(cvs_file_path)


def read_csv_file(file_path) -> list:
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data


def write_csv_file(file_path, data):
    file_exists = os.path.exists(file_path)

    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()
        writer.writerows(data)

