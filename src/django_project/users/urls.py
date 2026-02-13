from django.urls import path
from django_project.users import views


app_name = "users"
urlpatterns = [
    path("", views.ProfileDetailView.as_view(), name = "profile_page"),
    path("/update", views.ProfileUpdateView.as_view(), name="update_page"),
    path("/success", views.SuccessFeedbackView.as_view(), name = "success"),
]
