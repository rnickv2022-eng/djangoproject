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

print_posts:
	uv run ./src/django_project/manage.py print_posts

print_published_posts:
	uv run ./src/django_project/manage.py print_published_posts

create_post:
	uv run ./src/django_project/manage.py create_post

update_post:
	uv run ./src/django_project/manage.py update_post

delete_post:
	uv run ./src/django_project/manage.py delete_post

test_blog_app:
	uv run ./src/django_project/manage.py test blog_app

test_feedback_app:
	uv run ./src/django_project/manage.py test feedback_app

test:
	uv run ./src/django_project/manage.py test

test_verbose:
	uv run ./src/django_project/manage.py test -v 2

test_users:
	uv run ./src/django_project/manage.py test users
