#!/bin/sh 
sudo git pull origin main
source .env
poetry install
poetry run python osam_backend/manage.py makemigrations
poetry run python osam_backend/manage.py migrate
poetry run python osam_backend/manage.py collectstatic
sudo systemctl restart nginx
sudo systemctl restart gunicorn
