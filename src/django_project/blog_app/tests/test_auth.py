from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from django_project.blog_app.models import Category, Post


class AuthorizationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test-user", password="123456789q", is_staff=True)
        self.category = Category.objects.create(title="test-category")

    def test_create_post_anonymous(self):
        response = self.client.get(reverse("blog:create_post"))
        self.assertIn(reverse("users:login"), response.url)

    def test_create_post_authenticated(self):
        self.client.login(username="test-user", password="123456789q")
        response = self.client.get(reverse("blog:create_post"))
        self.assertEqual(response.status_code, 200)

    def test_create_post_submit(self):
        self.client.login(username="test-user", password="123456789q")
        response =  self.client.post(reverse("blog:create_post"), {
            "title":"post1",
            "content":"test-content",
            "topic":self.category.pk,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title="post1").exists())
