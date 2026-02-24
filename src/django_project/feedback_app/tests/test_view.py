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
        self.assertEqual(Feedback.objects.count(),1)

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
        self.assertEqual(Feedback.objects.count(), 0)
