run:
	uv run src/django_project/manage.py runserver
	uv run pre-commit run --all
