import csv
import json
import random
import datetime

today_date = datetime.datetime(2020, 1, 7)

def get_digit(raw_rut: int):
    str_rut = str(raw_rut)
    first_sum = 0
    numbers = [2, 3, 4, 5, 6, 7]
    j = 0
    for d in range(len(str_rut)):
        if j > 5:
            j = 0
        first_sum += int(str_rut[-d - 1]) * numbers[j]
        j += 1
    int_part = first_sum % 11
    number = 11 - int_part
    if number == 11:
        return 0
    elif number == 10:
        return "k"
    else:
        return number


def get_rut(int_rut: int):
    verify_digit = get_digit(int_rut)
    raw_rut = str(int_rut)
    return f"{raw_rut}-{verify_digit}"


with open('../data_files/Tecnicos.csv', 'r') as csv_file:
    csv_file_reader = csv.reader(csv_file, delimiter=',')

    with open('../osam_backend/backend_app/seed/0009_technician_seed.json', 'w', encoding='utf-8') as outfile:
        technician_list = []
        technician_id = 0
        for i, line in enumerate(csv_file_reader):
            if (i != 0):
                technician_id += 1

                nombres = line[2].replace("  ", " ").split(" ", 1)
                apellidos = line[1].replace("  ", " ").split(" ", 1)

                name = nombres[0].lower().capitalize()
                if len(nombres) != 1:
                    name += " " + nombres[1].lower().capitalize()

                last_name = apellidos[0].lower().capitalize()
                if len(apellidos) != 1:
                    last_name += " " + apellidos[1].lower().capitalize()
                
                if line[4] != "NULL":
                    mail = line[4].lower() 
                else:
                    mail = ""

                rut = get_rut(int(line[0]))

                password = apellidos[0] + "_" + line[1][len(line[1]) - 3:] + rut[-1]
                data = {
                    "model": "backend_app.technician",
                    "pk": technician_id,
                    "fields": {
                        "email": mail,
                        "first_name": name,
                        "last_name": last_name,
                        "rut": rut,
                        "phone": line[3],
                        "category_id": 1 if line[5]=="1" else 0,
                        "enterprise_id": int(line[7]),
                        "team_group_id": int(line[6]),
                        "last_audit_date": str(result_date)
                    }
                }
                technician_list.append(data)
        json.dump(technician_list, outfile, ensure_ascii=False)