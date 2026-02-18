from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django_project.users.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio","social_link","avatar"]
        widgets = {
            "bio": forms.TextInput()
        }
        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Коротко о себе",
                }
            ),
            "social_link": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите домашний сайт",
                }
            ),
            "avatar": forms.ClearableFileInput(
                attrs={
                    "class": "form-control"
                }
            )
        }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CustomCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Придумайте пароль",
                "autocomplete": "new-password",
            }
        )
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Подтвердите  пароль",
                "autocomplete": "new-password",
            }
        )
    )
    class  Meta:
        model = User
        fields = ["username","email","password1","password2"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите имя пользователя",
                    "autocomplete": "username",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите email",
                    "autocomplete": "email",
                }
            )
        }

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Пользователь с таким Email уже зарегистрирован")
        return email

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите имя",
                "autocomplete": "username",
            }
        )
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите свой пароль",
                "autocomplete": "current-password",
            }
        )
    )
