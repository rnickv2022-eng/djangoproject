from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from ninja import Router
from django.contrib.auth.models import User
from ninja.errors import HttpError
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail

from django_project.ninja_api.schemas import RegisterOutSchema, RegisterInSchema

auth_router = Router(tags=["Authentication"])

@auth_router.post("/register", response=RegisterOutSchema)
def register(request, payload:RegisterInSchema) -> RegisterOutSchema:
    if User.objects.filter(email=payload.email).exists():
        raise HttpError(status_code=400, message="Email уже  используется")
    if User.objects.filter(username=payload.username).exists():
        raise HttpError(status_code=400, message="Пользователь с таким  логином уже существует")

    user  = User.objects.create_user(
        username=payload.username,
        email=payload.email,
        password=payload.password,
        is_active=False,
    )

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    activation_url = f"http://http://127.0.0.1:8000/api/v2/auth/activate/{uid}/{token}"

    send_mail(
        subject="Подтверждение регистрации",
        message=f"Для подтверждения регистрации пройдите по ссылке: {activation_url}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )

    return RegisterOutSchema(message="Регистрация прошла успешно",
        username=user.username,
        email=user.email,
        id=user.id,
    )
