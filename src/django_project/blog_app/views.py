from django_project.blog_app.models import Post
from django_project.blog_app.models import Category
from django.shortcuts import get_object_or_404, render


def index(request):
    posts = Post.objects.filter(published = True).order_by("created_at")[:5]

    context = {
        "posts":posts
    }

    return render(request, template_name="blog_app/index.html", context=context)

def post_list(request):
    posts = Post.objects.filter(published = True)

    context = {
        "posts":posts
    }

    return render(request, template_name="blog_app/post_list.html", context=context)

def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {
        "post":post
    }
    return render(request, template_name="blog_app/post_detail.html", context=context )

def categories_list(request):
    categories = Category.objects.all()
    context = {
        "categories":categories
    }
    return render(request, template_name="blog_app/categories_list.html", context=context )

def category_detail(request, category_id):
    сategory_1 = get_object_or_404(Category, pk = category_id)
    posts = Post.objects.filter(topic=сategory_1)
    context = {
        "posts":posts,
        "category_name":сategory_1
    }
    return render(request, template_name="blog_app/category_detail.html", context=context )
