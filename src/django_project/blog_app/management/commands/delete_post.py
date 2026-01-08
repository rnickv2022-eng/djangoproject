from django.core.management.base import BaseCommand
from django_project.blog_app.models import Post

class Command(BaseCommand):
    help = "Удаляет посты"

    def handle(self, *args, **options):
        print("Введите id удаляемой статьи")
        id_1 = str(input())
        i = False
        posts = Post.objects.all()
        for post in posts:
            if str(post.id) == id_1:
                i = True
                del_post = Post.objects.filter(id=id_1)
                del_post.delete()
                print("Статья удалена")
        if not i:
            print("Статья данным с данным id не найдена")
