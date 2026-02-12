from django.urls import reverse_lazy

from django_project.users.models import Profile
from django_project.users.mixins import StaffRequiredMixin
from django_project.users.forms import UserForm
from django.views.generic import UpdateView, TemplateView


class ProfileUpdateView(StaffRequiredMixin,UpdateView):
    model = Profile
    form_class = UserForm
    template_name = "users/update_profile.html"
    success_url = reverse_lazy("users:success")

    def get_object(self, queryset=None):
        profile, flag = self.model.objects.get_or_create(user=self.request.user)
        return profile


class SuccessFeedbackView(TemplateView):
    template_name = 'users/success_page.html'
