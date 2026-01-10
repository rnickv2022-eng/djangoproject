from django.core.management.base import BaseCommand
from django_project.blog_app.models import Post

class Command(BaseCommand):
    help = "выводит список всех статей с фильтрацйией по опубликованным"

    def handle(self, *args, **options):
        post_available = Post.objects.filter(published=True).exists()
        if post_available:
            posts = Post.objects.filter(published=True)
            for post in posts:
                self.stdout.write(f"{post.id} {post.title} {post.created_at:%Y-%m-%d} {post.author}")
        if not post_available:
            self.stdout.write(self.style.WARNING("Опубликованных статей нет"))
