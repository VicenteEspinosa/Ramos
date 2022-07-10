import csv
import json

with open('../data_files/Comunas.csv', 'r') as csv_file:
    csv_file_reader = csv.reader(csv_file, delimiter=',')

    with open('../osam_backend/backend_app/seed/0004_communes_seed.json', 'w', encoding='utf-8') as outfile:
        commune_list = []

        for i, line in enumerate(csv_file_reader):
            if i != 0:
                data = {
                    "model": "backend_app.commune",
                    "pk": line[0],
                    "fields": {
                        "name": line[1],
                        "province_id": int(line[2]),
                        "region_zona_att": int(line[3]),
                        "region_crm": int(line[4])
                    }
                }
                commune_list.append(data)
        json.dump(commune_list, outfile, ensure_ascii=False)
