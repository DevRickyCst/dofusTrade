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
	python manage.py makemigrations itemViewer
	python manage.py makemigrations characterManager
	python manage.py migrate
	python manage.py createsuperuser