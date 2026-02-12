from django import forms
from django_project.blog_app.models import Post, Category
from django_project.blog_app.management.commands import utils


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","content","topic","published"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название статьи",
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
    def clean(self):
        cleaned_data = super().clean()
        subject = cleaned_data.get("title")
        post_slug = utils.translit_1(subject)
        post_available = Post.objects.filter(slug=post_slug).exclude(pk=self.instance.pk).exists()
        if post_available:
            self.add_error("title", "Статья с данным названием уже существует")

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите название категории",
                }
            )
        }

    def clean(self):
        cleaned_data = super().clean()
        subject = cleaned_data.get("title")
        category_available = Category.objects.filter(title=subject).exclude(pk=self.instance.pk).exists()
        if category_available:
            self.add_error("title", "Категория с данным названием уже существует")
