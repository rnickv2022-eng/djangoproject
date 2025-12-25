from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def increase_title(self):
        return str(self.title)

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.PositiveIntegerField(default=0)
    topic = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, null=True)

    def increase_views_count(self):
        self.views_count = self.views_count + 1
        return self.views_count

    def increase_title(self):
        return str(self.title)
