from django.urls import path
from django_project.users import views


app_name = "users"
urlpatterns = [
    path("", views.ProfileUpdateView.as_view(), name = "profile_page"),
    path("/success", views.SuccessFeedbackView.as_view(), name = "success"),
]
