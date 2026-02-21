from django.test import TestCase

from django_project.blog_app.forms import PostForm
from django_project.blog_app.models import Category


class PostFormTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title="test-category", slug="test-category")

    def test_valid_form(self):
        data = {
            "title": "test-title",
            "content": "test-content",
            "category": self.category
        }
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_empty_title(self):
        data = {
            "title": "",
            "content": "test-content",
            "category": self.category
        }
        form = PostForm(data=data)
        with self.assertRaises(TypeError):
            self.assertFalse(form.is_valid())

    def test_empty_content(self):
        data = {
            "title": "test-title",
            "content": "",
            "category": self.category
        }
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("content", form.errors)
