import json
import csv
import os
from typing import Generator, Dict


def write_file_csv(json_user: Generator[Dict[str, str], None, None]) -> None:
    with open('in.csv', 'w', newline='') as csv_file:
        writer_csv = csv.writer(csv_file)
        writer_csv.writerow(['name', 'address', 'email'])

        for data in json_user:
            writer_csv.writerow([data['name'], data['address'], data['email']])


def filtering_file(filtered: list) -> Generator[Dict[str, str], None, None]:
    json_user = (i for i in filtered
                 if (i['phoneNumber'][:2] == '+1'
                     or i['phoneNumber'][0] == '1')
                 and '4.0 Safari' in i['userAgent'])

    return json_user


def read_file_json(r_file: str) -> list:
    with open(r_file, 'r') as json_file:
        modified = json.load(json_file)

    return modified


name_file = 'in.json'

if os.path.exists(name_file):
    read = read_file_json(name_file)
    filtering = filtering_file(read)
    write_file_csv(filtering)
else:
    print('Файл не найден!')
