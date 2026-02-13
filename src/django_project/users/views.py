from django.urls import reverse_lazy

from django_project.users.models import Profile
from django.http import HttpResponseForbidden
from django_project.users.forms import UserForm
from django.views.generic import UpdateView, TemplateView, DetailView

class ProfileDetailBase:
    model = Profile
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Вы не зарегистрированы")
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        profile, flag = self.model.objects.get_or_create(user=self.request.user)
        return profile


class ProfileDetailView(ProfileDetailBase,DetailView):

    context_object_name = "user"
    template_name = "users/detail_profile.html"


class ProfileUpdateView(ProfileDetailBase,UpdateView):

    form_class = UserForm
    template_name = "users/update_profile.html"
    success_url = reverse_lazy("users:success")


class SuccessFeedbackView(TemplateView):
    template_name = 'users/success_page.html'
