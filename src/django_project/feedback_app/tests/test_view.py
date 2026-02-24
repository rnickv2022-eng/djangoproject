from django.test import TestCase
from django_project.feedback_app.models import Feedback

class FeedbackFormTest(TestCase):

    def test_feedback_detail_context(self):
        first_amount_feedback = Feedback.objects.count()
        response = self.client.post("/feedback/",{
            "name":"Николай",
            "subject":"Жалоба",
            "email":"username@username.com",
            "message":"Message"
        }
                                    )
        self.assertEqual(response.status_code, 302)
        second_amount_feedback = Feedback.objects.count()
        self.assertEqual((first_amount_feedback + 1), second_amount_feedback)

    def test_feedback_detail_incorrect(self):
        response = self.client.post("/feedback/", {
            "name": "Николай",
            "subject": "Жалоба",
            "email": "",
            "message": "Message"
        }
                                    )
        self.assertEqual(response.status_code, 200)
