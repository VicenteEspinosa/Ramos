import subprocess
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir("../osam_backend/backend_app/seed") if isfile(join("../osam_backend/backend_app/seed/", f))]
for file in onlyfiles:
    subprocess.run(f"../osam_backend/manage.py loaddata ../osam_backend/backend_app/seed/{file}")
    print(f"Lista seed de {file}")
