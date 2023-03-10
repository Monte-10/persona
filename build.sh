#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

npm install bootstrap@5.1.3
npm install @popperjs/core@2.11.5

python manage.py collectstatic --no-input

python manage.py migrate
python manage.py createsu
