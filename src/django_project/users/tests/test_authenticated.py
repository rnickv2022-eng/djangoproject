from django.test import TestCase

class AuthenticatedTestCase(TestCase):
    def test_create_post_anonymous_redirect(self):
        response = self.client.get('/users/update/')
        self.assertEqual(response.status_code, 403)

    def test_create_login_redirect(self):
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)
