from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
from django_project.users import views
from django_project.users.views import CustomLoginView

app_name = "users"
urlpatterns = [
    path("", views.ProfileDetailView.as_view(), name = "profile_page"),
    path("update/", views.ProfileUpdateView.as_view(), name="update_page"),
    path("success/", views.SuccessProfileView.as_view(), name = "success"),
    path("register/", views.RegisterUserView.as_view(), name = "register"),
    path("login/", CustomLoginView.as_view(), name = "login"),
    path("logout/", LogoutView.as_view(), name = "logout"),
    path("password_change/", PasswordChangeView.as_view(template_name="users/password_change.html", success_url=reverse_lazy("users:password_change_done")), name = "password_change"),
    path("password_change_done/", PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name = "password_change_done"),
    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset.html',
                                                      email_template_name='users/password_reset_email.html',
                                                      success_url=reverse_lazy('users:password_reset_done')),
                                                      name='password_reset'),
    path("password_reset/done/", PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name = "password_reset_done"),
    path("password_reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',success_url=reverse_lazy('users:password_reset_complete')), name = "password_reset_confirm"),
    path("password_reset/complete/", PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name = "password_reset_complete"),
]
