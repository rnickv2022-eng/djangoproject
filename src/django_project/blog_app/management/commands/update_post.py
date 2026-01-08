from django.core.management.base import BaseCommand
from django_project.blog_app.models import Post

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
    help = "Обновляет наименования постов"

    def handle(self, *args, **options):
        print("Введите название поста, которое бы хотели обновить")
        title_1 = str(input())
        english_text_1 = translit_1(title_1)
        posts = Post.objects.all()
        i = False
        for post in posts:
            if str(post.slug) == english_text_1:
                i = True
                break
        if i:
            print("Данный пост найден, введите новое название поста")
            title_2 = str(input())
            english_text_2 = translit_1(title_2)
            Post.objects.filter(slug=english_text_1).update(title=title_2,slug=english_text_2)
            print("Статья обновлена")
        if not i:
            print("Данный пост не найден")
