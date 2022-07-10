import csv
import json

with open('../data_files/operaciones.csv', 'r') as csv_file:
    csv_file_reader = csv.reader(csv_file, delimiter=',')

    with open('../osam_backend/backend_app/seed/0005_questions_operaciones_seed.json', 'w', encoding='utf-8') as out:
        question_list = []

        for i, line in enumerate(csv_file_reader):
            id = 0
            if i == 0:
                for cell in line:
                    if id >= 26:
                        if cell[0].isnumeric():
                            question_name = cell.split(".", 1)[1]
                            if question_name[0] == " ":
                                question_name = question_name[1:]
                        else: # Preguntas tipo comentario
                            question_name = cell
                        

                        if "observaciones" in question_name.lower():
                            category = 4
                            possible_values = []

                        elif 204 <= (id-25) <= 304 or (id-25) == 311:
                            possible_values = ["SI", "NO", "N/A", "N/O"]
                            category = 0
                        else:
                            possible_values = ["SI", "NO", "N/A"]
                            category = 1

                        if id - 25 == 126:
                            question_name += " Herramientas"
                        elif id - 25 == 186:
                            question_name += " EPP"
                        elif id - 25 == 203:
                            question_name += " Vestimenta"
                        elif id - 25 == 287:
                            question_name += " Tareas en Terreno"
                        elif id - 25 == 305:
                            question_name += " Relacionamiento Cliente"

                        data = {
                            "model": "backend_app.question",
                            "pk": id - 25,
                            "fields": {
                                "category": category,
                                "options": {"possible_values": possible_values},
                                "value": question_name,
                                "status": True,
                                "category_id": 0
                            }
                        }
                        question_list.append(data)
                    id += 1
        json.dump(question_list, out, ensure_ascii=False)

# LLega hasta el id = 342

with open('../data_files/redes.csv', 'r') as csv_file:
    csv_file_reader = csv.reader(csv_file, delimiter=',')

    with open('../osam_backend/backend_app/seed/0006_questions_redes_seed.json', 'w', encoding='utf-8') as outfile:
        question_list = []

        for i, line in enumerate(csv_file_reader):
            id2 = 0
            if i == 0:
                for cell in line:
                    if id2 >= 29:
                        if cell[0].isnumeric():
                            if id2 == 151 or id2 == 152: # Preguntas mal hechas con '-'
                                question_name = cell.split("-", 1)[1][1:]
                            else:
                                question_name = cell.split(".", 1)[1]
                                if question_name[0] == " ":
                                    question_name = question_name[1:]
                        else: # Preguntas tipo comentario
                            question_name = cell

                        if "observaciones" in question_name.lower():
                            category = 4
                            possible_values = []

                        else:
                            possible_values = ["SI", "NO", "N/A"]
                            category = 1

                        if (id2 - 28 + 342) == 398:
                            question_name += " Herramientas"
                        elif (id2 - 28 + 342) == 411:
                            question_name += " EPP"
                        elif (id2 - 28 + 342) == 418:
                            question_name += " Vestimenta"
                        elif 419 <= (id2 - 28 + 342) <= 441:
                            question_name += " (Bencinera)"
                        elif 442 <= (id2 - 28 + 342) <= 464:
                            question_name += " (En el Sitio)"
                        elif (id2 - 28 + 342) == 499:
                            question_name += " Team Baja Altura"


                        data = {
                            "model": "backend_app.question",
                            "pk": id2 - 28 + 342,
                            "fields": {
                                "category": category,
                                "options": {"possible_values": possible_values},
                                "value": question_name,
                                "status": True,
                                "category_id": 1
                            }
                        }
                        question_list.append(data)
                    id2 += 1
        json.dump(question_list, outfile, ensure_ascii=False)
