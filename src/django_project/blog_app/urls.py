from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.IndexView.as_view(), name = "index"),
    path("posts_list/", views.PostListView.as_view(), name = "post_list"),
    path("post/<slug:post_slug>/", views.PostDetailView.as_view(), name = "post_detail"),
    path("categories/", views.CategoriesListView.as_view(), name = "categories_list"),
    path("categories/<int:category_id>/", views.CategoriesDetailView.as_view(), name = "category_detail"),
    path("create_post/", views.PostCreateView.as_view(), name="create_post"),
    path("categories/create/", views.CategoryCreateView.as_view(), name="create_category"),
    path("categories/<int:category_id>/edit", views.CategoryUpdateView.as_view(), name = "category_edit"),
    path("post/<slug:post_slug>/edit", views.PostUpdateView.as_view(), name = "post_edit"),
    path("post/<slug:post_slug>/delete", views.PostDeleteView.as_view(), name = "post_delete"),
    path('deleted/', views.SuccessDeleteView.as_view(), name='success_post_delete'),
]
