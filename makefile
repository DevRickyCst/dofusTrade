local:
	python manage.py runserver

import-statics:
	python manage.py insert_statics

import-items:
	python manage.py db-management --delete

lint:
	black .
	isort .

install:
	rm db.sqlite3
	rm -r itemViewer/migrations
	rm -r characterManager/migrations
	python manage.py makemigrations itemViewer
	python manage.py makemigrations characterManager
	python manage.py migrate
	python manage.py createsuperuser