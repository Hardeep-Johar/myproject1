#!/usr/bin/env bash
# exit on error
set -o errexit
pip install -r requirements.txt
#add-apt-repository ppa:ubuntugis/ppa && sudo apt-get update
#apt-get update
#apt-get install gdal-bin
#apt-get install libgdal-dev
#export CPLUS_INCLUDE_PATH=/usr/include/gdal
#export C_INCLUDE_PATH=/usr/include/gdal
#pip install GDAL
python manage.py makemigrations
python manage.py migrate
#echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin1', 'admin@example.com', 'pass')" | python manage.py shell
