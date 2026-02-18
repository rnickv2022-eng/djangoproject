from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(verbose_name="Коротко о себе")
    social_link = models.URLField(verbose_name="Домашний сайт")
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True, verbose_name="Аватар")

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.height > 300 or img.width > 300:
                img.thumbnail((300, 300))
                img.save(self.avatar.path)
