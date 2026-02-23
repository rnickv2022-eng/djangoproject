from django.test import TestCase

class AuthenticatedTestCase(TestCase):
    def test_create_post_anonymous_redirect(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 403)
