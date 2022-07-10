import json
import random

timestamps = ["2021-05-11T17:36:30.285+00:00", "2021-07-25T17:36:30.285+00:00", "2021-02-03T06:00:00.000+00:00"]
values = [
    {"1": ["De que color es la camioneta?", "SI"],
    "2": ["Tiene las herramientas adecuadas?", "SI"],
    "3": ["Tuvo problemas el técnico?", "NO"]},
    {"1": ["De que color es la camioneta?", "N/A"],
    "2": ["Tiene las herramientas adecuadas?", "NO"]},
    {"1": ["De que color es la camioneta?", "NO"]},
    {"2": ["Tiene las herramientas adecuadas?", "N/A"]},
    ]


with open('data_answers.json', 'w', encoding='utf-8') as outfile:
    answer_lists = []
    for i in range(600):
        data = {
            "model": "backend_app.answers",
            "pk": 0,
            "fields": {
                "exit_timestamp":  "2021-02-03T06:00:00.000Z",                
                "category": "0",
                "values": {
                    "1": ["De que color es la camioneta?", "Rojo"],
                    "2": ["Tiene las herramientas adecuadas?", "SI"],
                    "3": ["Tuvo problemas el técnico?", "NO"]
                },
                "metadata": {
                    "timestamp_data": {
                    "initial_time": "22:30:00",
                    "initial_date": "2021/05/25",
                    "final_timestamp": "2021-05-25T22:30:00.895000"
                    },
                    "auditor_data": {
                    "auditor_name": "Juan Perez",
                    "auditor_rut": "11.111.111-1",
                    "auditor_email": "jperez@osam.cl",
                    "auditor_phone": "997005316"
                    },
                    "technician_data": {
                    "number_of_technicians": "1",
                    "enterprise": "empresa",
                    "team_id": "",
                    "id_group_team": "",
                    "technicians": {
                        "technician_1": {
                                "technician_name": "Juan",
                                "technician_rut": "10.563.254-1",
                                "technician_phone": "133",
                                "technician_external_id": "15"
                            },
                        "technician_2": {
                                "technician_name": "technician_name",
                                "technician_rut": "technician_rut",
                                "phone": "technician_phone",
                                "external_id": "technician_external_id"
                            }
                    }
                    },
                    "location_data": {
                    "latitude": "33.5",
                    "longitude": "70.6",
                    "dpt_or_office": "bla",
                    "street_number": "1066",
                    "street_name": "Calle",
                    "zone_att": "1",
                    "zone_crm": "1",
                    "commune": "Rancagua",
                    "province": "Cachapoal",
                    "region": "VI"
                    },
                    "category_data": {
                    "audit_type": "Fuera de Cliente",
                    "service_type": "BAFI",
                    "audit_category": "0",
                    "task_type": "",
                    "task_number": "",
                    "audit_type_number": "0",
                    "service_type_number": "0",
                    "audit_category_number": "0"
                    },
                    "truck_data": {
                    "truck_type": "truck_type",
                    "truck_license": "truck_license"
                    },
                    "extras": {
                    "audit_done": "OK",
                    "comments_nok": "NO APLICA"
                    }
                }
            }
        }
        data["fields"]["category"] = str(random.randint(0,1))
        data["pk"] = i + 1
        data["fields"]["exit_timestamp"] = random.choice(timestamps)
        data["fields"]["values"] = random.choice(values)
        data["fields"]["metadata"]["timestamp_data"]["final_timestamp"] = data["fields"]["exit_timestamp"]
        answer_lists.append(data)
    json.dump(answer_lists, outfile)