import csv
import json

with open('../data_files/Empresas Ejecutoras.csv', 'r') as csv_file:
    csv_file_reader = csv.reader(csv_file, delimiter=',')

    with open('../osam_backend/backend_app/seed/0007_enterprise_seed.json', 'w', encoding='utf-8') as outfile:
        enterprise_list = []

        for i, line in enumerate(csv_file_reader):
            if i != 0:
                data = {
                    "model": "backend_app.enterprise",
                    "pk": line[0],
                    "fields": {
                        "name": line[1]
                    }
                }
                enterprise_list.append(data)
        json.dump(enterprise_list, outfile, ensure_ascii=False)
