from django.urls import reverse_lazy

from django_project.blog_app.mixins import TitleMixin, StaffRequiredMixin
from django_project.blog_app.models import Post
from django_project.blog_app.models import Category
from django_project.blog_app.forms import PostForm,CategoryForm
from django_project.blog_app.management.commands import utils
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexView(TitleMixin, TemplateView):
    template_name = "blog_app/index.html"
    title = "Самая главная страница"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(published = True).order_by("created_at")[:5]
        return context

class PostListView(ListView):
    model = Post
    template_name = "blog_app/post_list.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.filter(published = True)

class PostDetailView(DetailView):
    model = Post
    template_name = "blog_app/post_detail.html"
    context_object_name = "post"
    slug_url_kwarg = "post_slug"

class CategoriesListView(ListView):
    model = Category
    template_name = "blog_app/categories_list.html"
    context_object_name = "categories"
    paginate_by = 5

#  1  TODO  разобраться  в документации Джанго как эта функция работает
class CategoriesDetailView(ListView):
    model = Category
    template_name = "blog_app/category_detail.html"
    context_object_name = "posts"
    pk_url_kwarg = "category_id"
    paginate_by = 5

#  2 TODO  разобраться  в документации Джанго как эта функция работает
    def get_queryset(self):
        return Post.objects.filter(topic_id=self.kwargs['category_id'])

#  3 TODO  разобраться  в документации Джанго как эта функция работает
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

class PostCreateView(StaffRequiredMixin, CreateView):
    model = Post
    template_name = "blog_app/create_post.html"
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')

#  4  TODO  разобраться  в документации Джанго как эта функция работает
    def form_valid(self, form):
        form.instance.slug = utils.translit_1(form.cleaned_data["title"])
        form.instance.author = self.request.user
        return super().form_valid(form)

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    pk_url_kwarg = "category_id"
    template_name = "blog_app/create_category.html"


    def form_valid(self, form):
        form.instance.slug = utils.translit_1(form.cleaned_data["title"])
        return super().form_valid(form)


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    pk_url_kwarg = "category_id"
    template_name = "blog_app/create_category.html"

    def form_valid(self, form):
        form.instance.slug = utils.translit_1(form.cleaned_data["title"])
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    slug_url_kwarg = "post_slug"
    template_name = "blog_app/create_post.html"
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        form.instance.slug = utils.translit_1(form.cleaned_data["title"])
        return super().form_valid(form)

#  5  TODO  разобраться  в документации Джанго как эта фция работает
class  PostDeleteView(DeleteView):
     model = Post
     template_name = "blog_app/post_delete.html"
     context_object_name = "post"
     slug_url_kwarg = "post_slug"
     success_url = reverse_lazy("blog:success_post_delete")

#  6  TODO  разобраться  в документации Джанго как эта функция работает
class SuccessDeleteView(TemplateView):
    template_name = "blog_app/success_post_delete.html"
