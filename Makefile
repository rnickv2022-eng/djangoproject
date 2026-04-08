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

check:
	uv run src/django_project/manage.py check

dump:
	uv run src/django_project/manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > fixtures/datadump.json

restore:
	uv run src/django_project/manage.py loaddata fixtures/datadump.json

create_db:
	docker run \
	--name blog_db \
	-e POSTGRES_USER=myuser \
	-e POSTGRES_PASSWORD=mypassword \
	-e POSTGRES_DB=mydb \
	-p 5432:5432 \
	-v blog_db_data:/var/lib/postgresql/data \
 	-d postgres:17

start_db:
	docker start blog_db

stop_db:
	docker stop blog_db

remove_db:
	docker rm blog_db

remove_db_force:
	docker rm -f blog_db

remove_storage:
	docker volume rm blog_db_data

create_container:
	docker run \
	--name blog \
	--network blog_net \
	-p 8000:8000 \
	--env-file .env \
	-d blog_image

create_image:
	docker build -t blog_image .

delete_container:
	docker rm -f blog

in_container:
	docker exec -it blog bash

delete_image:
	docker rmi blog_image

db_blog_net:
	docker run \
	--name blog_db \
	--network blog_net \
	-e POSTGRES_USER=myuser \
	-e POSTGRES_PASSWORD=mypassword \
	-e POSTGRES_DB=mydb \
	-v blog_db_data:/var/lib/postgresql/data \
	-d postgres:17

connecting_storage:
	docker run --name blog \
	--network blog_net \
	-p 8000:8000 \
	--env-file .env \
	-v .src/django_project/media/:/app/src/django_project/media/ \
	-d blog_image

run_all: migrate restore
	uv run src/django_project/manage.py runserver 0.0.0.0:8000

compose_start:
	docker compose up -d

compose_rebuild:
	docker compose up -d --build

compose_logs:
	docker compose logs -f
