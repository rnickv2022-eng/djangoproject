from django.core.management.base import BaseCommand
from django_project.blog_app.models import Post
from django.contrib.auth.models import User

def translit_1(str_1): #Программа для транслитерации
    str_2 = ""
    ru_eng = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
        'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya',
        'А': 'a', 'Б': 'b', 'В': 'v', 'Г': 'g', 'Д': 'd',
        'Е': 'e', 'Ё': 'yo', 'Ж': 'zh', 'З': 'z', 'И': 'i',
        'Й': 'y', 'К': 'k', 'Л': 'l', 'М': 'm', 'Н': 'n',
        'О': 'o', 'П': 'p', 'Р': 'r', 'С': 's', 'Т': 't',
        'У': 'u', 'Ф': 'f', 'Х': 'kh', 'Ц': 'ts', 'Ч': 'ch',
        'Ш': 'sh', 'Щ': 'sch', 'Ы': 'y', 'Э': 'e', 'Ю': 'yu', 'Я': 'ya'
    }
    for i in range(len(str_1)):
        if str_1[i] in ru_eng:
            str_2 = str_2 + ru_eng[str_1[i]]
        else:
            str_2 = str_2 + str_1[i]

    return str_2


class Command(BaseCommand):
    help = "Создает посты"

    def handle(self, *args, **options):
        print("Введите тему")
        title_1 = str(input())
        english_text = translit_1(title_1)

        print("Введите содержание")
        content_1 = str(input())

        while True:
            print("Введите автора")
            i = False
            author_1 = str(input())
            posts = User.objects.all()
            for post in posts:
                if author_1 == str(post):
                    author_1 = post
                    i = True
                    break
            if i:
                print("Данный автор есть")
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
        new_post = Post.objects.create(title=title_1, content=content_1, author=author_1, published=published_1, slug=english_text)
        new_post.save
        print("Статья добавлена")
