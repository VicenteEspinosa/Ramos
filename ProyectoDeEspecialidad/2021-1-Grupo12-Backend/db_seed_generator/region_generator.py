import csv
import json

with open('../data_files/Regiones.csv', 'r') as csv_file:
    csv_file_reader = csv.reader(csv_file, delimiter=',')

    with open('../osam_backend/backend_app/seed/0002_regions_seed.json', 'w', encoding='utf-8') as outfile:
        region_list = []

        for i, line in enumerate(csv_file_reader):
            if i != 0:
                data = {
                    "model": "backend_app.region",
                    "pk": line[0],
                    "fields": {
                        "name": line[1],
                        "region_ordinal": line[2]
                    }
                }
                region_list.append(data)
        json.dump(region_list, outfile, ensure_ascii=False)
