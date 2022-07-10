import csv
import json
with open('../data_files/Teams.csv', 'r') as csv_file:
    csv_file_reader = csv.reader(csv_file, delimiter=',')
    with open('../osam_backend/backend_app/seed/0016_teams_seed.json', 'w', encoding='utf-8') as outfile:
        team_list = []
        for i, line in enumerate(csv_file_reader):
            if i != 0:
                data = {
                    "model": "backend_app.team",
                    "pk": line[0],
                    "fields": {
                        "name": line[2],
                        "code": line[1]
                    }
                }
                team_list.append(data)
        json.dump(team_list, outfile, ensure_ascii=False)