from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, reverse_lazy
from django_project.users import views


app_name = "users"
urlpatterns = [
    path("", views.ProfileDetailView.as_view(), name = "profile_page"),
    path("update/", views.ProfileUpdateView.as_view(), name="update_page"),
    path("success/", views.SuccessProfileView.as_view(), name = "success"),
    path("register/", views.RegisterUserView.as_view(), name = "register"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name = "login"),
    path("logout/", LogoutView.as_view(), name = "logout"),
    path("password_change/", PasswordChangeView.as_view(template_name="users/password_change.html", success_url=reverse_lazy("users:password_change_done")), name = "password_change"),
    path("password_change_done/", PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name = "password_change_done"),
]
