from django.test import TestCase
from django_project.feedback_app.models import Feedback

class FeedbackFormTest(TestCase):

    def test_feedback_detail_context(self):
        response = self.client.post("/feedback/",{
            "name":"Николай",
            "subject":"Жалоба",
            "email":"username@username.com",
            "message":"Message"
        }
                                    )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(1, Feedback.objects.count())

    def test_feedback_detail_incorrect(self):
        response = self.client.post("/feedback/", {
            "name": "Николай",
            "subject": "Жалоба",
            "email": "",
            "message": "Message"
        }
                                    )
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertFalse(form.is_valid())
        self.assertEqual(0, Feedback.objects.count())
