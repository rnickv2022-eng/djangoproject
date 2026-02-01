from django_project.blog_app.models import Post
from django_project.blog_app.models import Category
from django.shortcuts import get_object_or_404, render
from django_project.blog_app.forms import PostForm,CategoryForm
from django.shortcuts import redirect
from django_project.blog_app.management.commands import utils


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
        "category_name":сategory_1,
        "category_id":category_id
    }
    return render(request, template_name="blog_app/category_detail.html", context=context )

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if  form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = utils.translit_1(new_post.title)
            new_post.save()
            return redirect("blog:post_detail",new_post.slug)
    else:
        form = PostForm()

    context = {
        "form":form
    }
    return render(request, "blog_app/create_post.html",context=context)

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if  form.is_valid():
            new_category = form.save(commit=False)
            new_category.slug = utils.translit_1(new_category.title)
            new_category.save()
            return redirect("blog:category_detail",new_category.id)
    else:
        form = CategoryForm()

    context = {
        "form":form
    }
    return render(request, "blog_app/create_category.html",context=context)

def category_edit(request,category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=category)

        if  form.is_valid():
            new_category = form.save(commit=False)
            new_category.slug = utils.translit_1(new_category.title)
            new_category.save()
            return redirect("blog:category_detail",new_category.id)
    else:
        form = CategoryForm(instance=category)

    context = {
        "form":form
    }
    return render(request, "blog_app/create_category.html",context=context)

def post_edit(request,post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)

        if  form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = utils.translit_1(new_post.title)
            new_post.save()
            return redirect("blog:post_detail",new_post.slug)
    else:
        form = PostForm(instance=post)

    context = {
        "form":form
    }
    return render(request, "blog_app/create_post.html",context=context)
