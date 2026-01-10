from django.core.management.base import BaseCommand
from django_project.blog_app.models import Post
from .utils import translit_1

class Command(BaseCommand):
    help = "Обновляет наименования постов"

    def handle(self, *args, **options):
        while True:
            print("Введите по какому критерию хотите осуществить поиск статьи: название(1) или id(2) (ввести 1/2)")
            poisk = str(input())
            if poisk == "1" or poisk == "2":
                break

        if poisk == "1":
            print("Введите название поста, которое бы хотели обновить")
            title_1 = str(input())
            english_title_1 = translit_1(title_1)
            post_available = Post.objects.filter(slug=english_title_1).exists()

        if poisk == "2":
            print("Введите id поста, которое бы хотели обновить")
            id_1 = str(input())
            post_available = Post.objects.filter(id=id_1).exists()

        if post_available:
                print("Данный пост найден, введите новое название поста")
                title_2 = str(input())
                english_title_2 = translit_1(title_2)
                if poisk == "1":
                    Post.objects.filter(slug=english_title_1).update(title=title_2,slug=english_title_2)
                    print("Статья обновлена")
                if poisk == "2":
                    Post.objects.filter(id=id_1).update(title=title_2,slug=english_title_2)
                    print("Статья обновлена")
        if not post_available:
            print("Статья данным с данным названием не найдена")
