from django.contrib.auth.models import User
from django.test import TestCase
from django_project.blog_app.models import Category, Post
from django.db import IntegrityError


class PostModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test-user", password="123456789q")
        self.category = Category.objects.create(title="test-category", slug="test-category")
        self.post = Post.objects.create(title="test-title", slug="test-slug", content="test-content", topic=self.category, author=self.user)

    def test_post_creation(self):
        self.assertEqual(self.post.title, "test-title")
        self.assertEqual(self.post.slug, "test-slug")
        self.assertEqual(self.post.topic, self.category)
        self.assertFalse(self.post.published)

    def test_post_str(self):
        self.assertEqual(str(self.post), "test-title")

class CategoryModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test-user", password="123456789q")
        self.category = Category.objects.create(title="test-category-title", slug="test-category-slug")

    def test_category_creation(self):
        self.assertEqual(self.category.title, "test-category-title")
        self.assertEqual(self.category.slug, "test-category-slug")

    def test_category_str(self):
        self.assertEqual(str(self.category), "test-category-title")

    def test_category_creation_duo(self):
        Category.objects.create(title="test-category-title-1", slug="test-category-slug-1")
        with self.assertRaises(IntegrityError):
            Category.objects.create(title="test-category-title-1", slug="test-category-slug-1")
