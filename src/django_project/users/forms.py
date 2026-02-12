from django import forms
from django_project.users.models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio","social_link"]
        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите биографию",
                }
            ),
            "social_link": forms.URLInput(
                attrs={
                    "class": "form-select",
                    "placeholder": "Введите домашний сайт",
                }
            )
        }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
