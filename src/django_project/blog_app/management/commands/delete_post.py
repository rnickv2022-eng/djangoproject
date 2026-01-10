from django.core.management.base import BaseCommand
from django_project.blog_app.models import Post

class Command(BaseCommand):
    help = "Удаляет посты"

    def handle(self, *args, **options):
        print("Введите id удаляемой статьи")
        id_1 = str(input())
        post_available = Post.objects.filter(id=id_1).exists()
        if post_available:
                Post.objects.filter(id=id_1).delete()
                print("Статья удалена")
        if not post_available:
            print("Статья данным с данным id не найдена")
