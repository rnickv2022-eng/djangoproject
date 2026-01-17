from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path("", views.index, name = "index"),
    path("posts_list/", views.post_list, name = "post_list"),
    path("post/<str:post_slug>/", views.post_detail, name = "post_detail"),
    path("categories/", views.categories_list, name = "categories_list"),
    path("categories/<int:category_id>/", views.category_detail, name = "category_detail"),
]
