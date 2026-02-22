from django_project.blog_app.models import Category, Post
from django_project.users.models import Profile


def categories_processor(request):
    return {
        'nav_categories': Category.objects.all()
    }

def blog_stats_processor(request):
    return {
        "total_posts": Post.objects.all().count(),
        "total_users": Profile.objects.all().count()
    }
