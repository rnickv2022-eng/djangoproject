run:
	uv run src/django_project/manage.py runserver

lint:
	uv run pre-commit run --all

makemigrations:
	uv run ./src/django_project/manage.py makemigrations

migrate:
	uv run ./src/django_project/manage.py migrate

createsuperuser:
	uv run ./src/django_project/manage.py createsuperuser
