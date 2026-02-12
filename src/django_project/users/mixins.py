from django.http import HttpResponseForbidden


class TitleMixin:
    title = None

class StaffRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Вы не зарегистрированы")
        return super().dispatch(request, *args, **kwargs)
