from django.core.management.base import BaseCommand
from django_project.blog_app.models import Post

class Command(BaseCommand):
    help = "выводит список всех статей с фильтрацйией по опубликованным"

    def handle(self, *args, **options):
        posts = Post.objects.all()
        i_1 = False
        for post in posts:
            if post.published:
                self.stdout.write(f"{post.id} {post.title} {post.created_at:%Y-%m-%d} {post.author}")
                i_1 = True
        if not i_1:
            self.stdout.write(self.style.WARNING("Опубликованных статей нет"))
