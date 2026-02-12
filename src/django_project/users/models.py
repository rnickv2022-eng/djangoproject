from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(verbose_name="Биография")
    social_link = models.URLField(verbose_name="Домашний сайт")


    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"
