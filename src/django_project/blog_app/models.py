from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=100,verbose_name="Название")
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:category_detail", args=[self.id])


class Post(models.Model):
    title = models.CharField(max_length=255,verbose_name="Название")
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name="Содержание")
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Автор")
    published = models.BooleanField(default=False,verbose_name="Опубликовать?")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Дата обновления")
    views_count = models.PositiveIntegerField(default=0,verbose_name="Количестиво просмотров")
    topic = models.ForeignKey(Category,on_delete=models.CASCADE,default=1, null=True,related_name="posts",verbose_name="Категории")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["created_at","published"]

    def increase_views_count(self):
        self.views_count = self.views_count + 1
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.slug])
