# from django.contrib.auth.hashers import make_password
# import json
# adder = make_password
# jsonfunct = json

# FIRST EXECUTE user_generator.py


def password_adder(adder, jsonfunct):
    with open('osam_backend/backend_app/seed/0006_user_seed_unencripted.json', 'r') as file_original:
        with open('osam_backend/backend_app/seed/0006_user_seed_encrypted.json', 'w') as file_new:
            user_list = []
            file_original = jsonfunct.load(file_original)
            for data in file_original:
                new_password = adder(data["fields"]["password"])
                data["fields"]["password"] = new_password
                user_list.append(data)
            jsonfunct.dump(user_list, file_new, ensure_ascii=False)


# Run this in shell:
# from django.contrib.auth.hashers import make_password
# import json as Json
# from db_seed_generator.encrypt_user_seed import password_adder
# password_adder(make_password, Json)