local:
	python manage.py runserver

import-statics:
	python manage.py insert_statics

filldb:
	python manage.py db-management

lint:
	black .
	isort .

install:
	python manage.py makemigrations itemViewer
	python manage.py makemigrations characterManager
	python manage.py migrate
	python manage.py createsuperuser