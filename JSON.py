import json
import csv


with open('in.json', newline='') as json_file:
    reader_json = json.load(json_file)
    json_user = (i for i in reader_json
                 if (i['phoneNumber'][:2] == '+1' or
                     i['phoneNumber'][0] == '1') and
                 '4.0 Safari' in i['userAgent'])

with open('in.csv', 'w', newline='') as csvfile:
    writer_csv = csv.writer(csvfile, delimiter=',')
    writer_csv.writerow(['name', 'address', 'email'])

    for data in json_user:
        writer_csv.writerow([data['name'], data['address'], data['email']])
