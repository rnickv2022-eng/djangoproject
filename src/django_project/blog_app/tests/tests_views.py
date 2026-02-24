from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from django_project.blog_app.models import Category, Post

class PostViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test-user", password="123456789q")
        self.category = Category.objects.create(title="test-category", slug="test-category")
        self.post = Post.objects.create(title="test-title", slug="test-slug", content="test-content",
                                        topic=self.category, author=self.user, published=True)

    def test_index_status_code(self):
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)

    def  test_index_template(self):
        response = self.client.get(reverse("blog:index"))
        self.assertTemplateUsed(response, "blog_app/index.html")

    def test_index_contains_post(self):
        response = self.client.get(reverse("blog:index"))
        self.assertContains(response, "test-title")

    def test_post_detail_status_code(self):
        response = self.client.get(reverse("blog:post_detail", args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_template(self):
        response = self.client.get(reverse("blog:post_detail", args=[self.post.slug]))
        self.assertTemplateUsed(response, "blog_app/post_detail.html")

    def test_post_detail_context(self):
        response = self.client.get(reverse("blog:post_detail", args=[self.post.slug]))
        self.assertEqual(response.context["post"], self.post)

    def test_post_detail_404(self):
        response = self.client.get(reverse("blog:post_detail", args=["Page-doesnt-exist"]))
        self.assertEqual(response.status_code, 404)

    def test_index_not_have_unpublished(self):
        Post.objects.create(title="test-title2", slug="test-slug2", content="test-content2",
                                        topic=self.category, author=self.user, published=False)
        response = self.client.get(reverse("blog:index"))
        self.assertNotContains(response, "test-title2")
        self.assertContains(response, "test-title")

class CreateViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test-user", password="123456789q")
        self.category_first = Category.objects.create(title="test-category-first", slug="test-category-first")
        self.category_second = Category.objects.create(title="test-category-second", slug="test-category-second")
        self.post_first = Post.objects.create(title="test-title-first", slug="test-slug-first", content="test-content",
                                        topic=self.category_first, author=self.user, published=True)
        self.post_second = Post.objects.create(title="test-title-second", slug="test-slug-second", content="test-content",
                                         topic=self.category_second, author=self.user, published=True)

    def  test_filter_category(self):
        response = self.client.get(f"/categories/{self.category_first.id}/")
        self.assertContains(response, "test-title-first")
        self.assertNotContains(response, "test-title-second")
        response = self.client.get(f"/categories/{self.category_second.id}/")
        self.assertContains(response, "test-title-second")
        self.assertNotContains(response, "test-title-first")

    # TODO  Dont work!
    def test_category_id_nothing(self):
        last_obj = Category.objects.last()
        new_id =  int(last_obj.pk +  100)
        response = self.client.get(f"/categories/{new_id}/")
        self.assertEqual(response.status_code, 404)
