from django.urls import path
from django_project.feedback_app import views


app_name = "feedback"
urlpatterns = [
    path("", views.FeedbackCreateView.as_view(), name = "feedback_page"),
    path("success/", views.SuccessFeedbackView.as_view(), name = "success"),
]
