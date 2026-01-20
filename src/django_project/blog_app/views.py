from django.http import HttpResponse
from django_project.blog_app.models import Post
from django_project.blog_app.models import Category
from django.shortcuts import get_object_or_404


def index(request):
    return HttpResponse("<h1>Hellow blog</h1>")

def post_list(request):
    posts = Post.objects.filter(published = True)
    if not posts:
        response_content = "<h1> Статей пока нет. </h1> <ul>"
        return HttpResponse(response_content)
    response_content = "<h1>Список статей</h1> <ul>"
    for post in posts:
       response_content = response_content + f'<li><a href="/post/{post.slug}/">{post.title}</a> {post.created_at}</li>'
    response_content = response_content + "</ul>"
    return HttpResponse(response_content)

def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    content = f'''
    <h1>{post.title}</h1>
    <p>автор: {post.author.username}</p>
    <div> контент:{post.content} </div>
    <hr>
    <a href="/posts_list/">Назад к статьям</a>
    '''
    return HttpResponse(content)

def categories_list(request):
    categories = Category.objects.all()
    response_content = "<h1>Список категорий</h1> <ul>"
    for сategory_1 in categories:
       response_content = response_content + f'<li><a href="/categories/{сategory_1.id}">{сategory_1.title}</a> </li>'
    response_content = response_content + "</ul>"
    return HttpResponse(response_content)

def category_detail(request, category_id):
    сategory_1 = get_object_or_404(Category, pk = category_id)
    posts = Post.objects.filter(topic=сategory_1)
    if not posts:
        response_content = f"<h1> В категории: {сategory_1.title}, статей нет. </h1> <ul>"
        return HttpResponse(response_content)
    response_content = f"<h1> Категория: {сategory_1.title} </h1> <ul>"
    response_content += '<li><a href="/categories/">Перейти к категориям </a>'
    for post in posts:
        if post.published:
            post_published = "Да"
        else:
            post_published = "Нет"
        response_content += f'''
        <h2>{post.title}</h2>
        <p>автор: {post.author.username}</p>
        <div> контент:{post.content} </div>
        <div> публикация:{post_published} </div>
        <hr>
        <a href="/post/{post.slug}/">Перейти к статье</a>
        '''
    return HttpResponse(response_content)
