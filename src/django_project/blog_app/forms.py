from django import forms
from django_project.blog_app.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","author","content","topic","published"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название статьи",
                }
            ),
            "author": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
            "cathegory": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите содержание статьи",
                    "rows":10
                }
            ),
            "published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input"
                }
            )

        }
