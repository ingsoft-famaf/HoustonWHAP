rm db.sqlite3;
rm -r gst/migrations;
python manage.py makemigrations;
python manage.py migrate;
python manage.py migrage --run-syncdb;
python manage.py createsuperuser;
