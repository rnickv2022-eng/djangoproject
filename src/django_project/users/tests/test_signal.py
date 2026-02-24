from unittest import TestCase
from django.contrib.auth.models import User
from django_project.users.models import Profile


class SignalUserCreateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser123', password='testpass123', is_staff=True)
        self.user.save()

    def test_create_user_signal(self):
        self.assertTrue(Profile.objects.filter(user=self.user))
