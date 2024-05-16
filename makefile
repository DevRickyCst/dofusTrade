local:
	python manage.py runserver

import-statics:
	python manage.py insert_statics

filldb:
	python manage.py db-management

lint:
	black .
	isort .