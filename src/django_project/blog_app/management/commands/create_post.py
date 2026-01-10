from django.core.management.base import BaseCommand
from django_project.blog_app.models import Post
from django.contrib.auth.models import User
from .utils import translit_1


class Command(BaseCommand):
    help = "Создает посты"

    def handle(self, *args, **options):
        while True:
            print("Введите тему")
            title_1 = str(input())
            english_title_1 = translit_1(title_1)
            post_available = Post.objects.filter(slug=english_title_1).exists()
            if not post_available:
                print("Статьи с данным названием нет")
                break
            else:
                print("Статья с даным названием есть")

        print("Введите содержание")
        content_1 = str(input())

        while True:
            print("Введите автора")
            author_0 = str(input())
            author_available = User.objects.filter(username=author_0).exists()
            if author_available:
                print("Данный автор есть")
                author_1 = User.objects.get(username=author_0)
                break
            else:
                print("Данный автор отсутствует")

        while True:
            print("Опубликовать? (да/нет)")
            publ = input()
            if publ == "да":
                published_1 = True
                break
            if publ == "нет":
                published_1 = False
                break
        Post.objects.create(title=title_1, content=content_1, author=author_1, published=published_1, slug=english_title_1)
        print("Статья добавлена")
