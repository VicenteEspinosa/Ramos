import csv
import json

with open('../data_files/Provincias.csv', 'r') as csv_file:
    csv_file_reader = csv.reader(csv_file, delimiter=',')

    with open('../osam_backend/backend_app/seed/0003_provinces_seed.json', 'w', encoding='utf-8') as outfile:
        province_list = []

        for i, line in enumerate(csv_file_reader):
            if i != 0:
                data = {
                    "model": "backend_app.province",
                    "pk": line[0],
                    "fields": {
                        "name": line[1],
                        "region_id": int(line[2])
                    }
                }
                province_list.append(data)
        json.dump(province_list, outfile, ensure_ascii=False)
