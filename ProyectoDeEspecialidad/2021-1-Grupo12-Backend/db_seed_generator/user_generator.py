import csv
import json

# EXECUTE encrypt_user_seed.py after this


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
    
    
with open('../data_files/Auditores.csv', 'r') as csv_file:
    csv_file_reader = csv.reader(csv_file, delimiter=',')

    with open('../osam_backend/backend_app/seed/0006_user_seed_unencripted.json', 'w', encoding='utf-8') as outfile:
        user_list = []
        user_id = 0
        for i, line in enumerate(csv_file_reader):
            if (i != 0) and (i != 4):
                user_id += 1

                if i == 6: # Juan
                    _type = 1
                else: # Otros
                    _type = 2

                nombres = line[3].split(" ", 1)
                apellidos = line[2].split(" ", 1)
                username = nombres[0][0].lower()
                if len(nombres) != 1:
                    second_name = nombres[1]
                    username += second_name[0].lower()
                last_name = apellidos[0]
                username += last_name.lower()

                name = nombres[0].lower().capitalize()
                if len(nombres) != 1:
                    name += " " + nombres[1].lower().capitalize()

                last_name = apellidos[0].lower().capitalize()
                if len(apellidos) != 1:
                    last_name += " " + apellidos[1].lower().capitalize()
                rut = get_rut(int(line[1]))
                password = apellidos[0] + "_" + line[1][len(line[1]) - 3:] + rut[-1]
                data = {
                    "model": "backend_app.user",
                    "fields": {
                        "username": username,
                        "user_id": user_id,
                        "email": line[4],
                        "first_name": name,
                        "last_name": last_name,
                        "password": password,
                        "rut": rut,
                        "_type": _type,
                        "category_id": -1,
                        "access_token": "Null",
                        "access_token_mobile": "Null",
                    }
                }
                user_list.append(data)
        json.dump(user_list, outfile, ensure_ascii=False)
