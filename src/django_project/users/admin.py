from django.contrib import admin
from django_project.users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id","user","bio","social_link")
    search_fields = ("user","bio")
    list_filter = ("user","social_link")
