from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(verbose_name="Коротко о себе")
    social_link = models.URLField(verbose_name="Домашний сайт")
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True, verbose_name="Аватар")
    original_avatar_name = models.CharField(verbose_name="Изначальное имя файла", default="")

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"

    def save(self, *args, **kwargs):
        if self.avatar:
            self.original_avatar_name = self.avatar.name
            if self.pk:
                old_profile_avatar_name = Profile.objects.get(pk=self.pk).original_avatar_name
            else:
                old_profile_avatar_name = None
            if old_profile_avatar_name != self.original_avatar_name:
                super().save(*args, **kwargs)
                img = Image.open(self.avatar.path)
                if img.height > 300 or img.width > 300:
                    img.thumbnail((300, 300))
                    img.save(self.avatar.path)
                    super().save(*args, **kwargs)
            else:
                super().save(update_fields=["user","bio","social_link"],*args, **kwargs)
        else:
            super().save(*args, **kwargs)
