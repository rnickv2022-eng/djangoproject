from django.urls import reverse_lazy

from django_project.feedback_app.forms import FeedbackForm
from django.views.generic import TemplateView, FormView

from django_project.feedback_app.models import Feedback


class FeedbackCreateView(FormView):
    template_name = 'feedback_app/feedback_page.html'
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback:success')

    def form_valid(self, form):
        Feedback.objects.create(**form.cleaned_data)
        return super().form_valid(form)


class SuccessFeedbackView(TemplateView):
    template_name = 'feedback_app/success_page.html'
