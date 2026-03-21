from django.conf import settings
from django.contrib.auth import aauthenticate
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from ninja import Router
from django.contrib.auth.models import User
from ninja.errors import HttpError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from django_project.ninja_api.schemas import RegisterOutSchema, RegisterInSchema, ActivateOutSchema, LoginOutSchema, \
    LoginInSchema

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

    activation_url = f"http://127.0.0.1:8000/api/v2/auth/activate/{uid}/{token}"
    context = {
        "activation_url": activation_url,
        "user": user,
        "site_name": "django blog",
    }

    html_content = render_to_string("email/activation_email.html", context)

    #send_mail(
    #    subject="Подтверждение регистрации",
    #    message=f"Для подтверждения регистрации пройдите по ссылке: {activation_url}",
    #    from_email=settings.DEFAULT_FROM_EMAIL,
    #    recipient_list=[user.email],
    #    fail_silently=False,
    #)

    message = EmailMessage(
        subject="Подтверждение регистрации",
        body=html_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
    )
    message.content_subtype = "html"

    message.send()

    return RegisterOutSchema(message="Регистрация прошла успешно",
        username=user.username,
        email=user.email,
        id=user.id,
    )

@auth_router.get("/activate/{uid}/{token}", response=ActivateOutSchema)
async def activate(request, uid:str, token:str) -> ActivateOutSchema:
    try:
        user_id = urlsafe_base64_decode(force_str(uid))
        user = await User.objects.aget(pk=user_id)
    except (TypeError, ValueError, User.DoesNotExist):
        return ActivateOutSchema(message="Ошибка активации", activated=False)

    if not default_token_generator.check_token(user, token):
        return ActivateOutSchema(message="Неверный токен", activated=False)

    user.is_active = True
    await user.asave()

    return ActivateOutSchema(message="Пользователь активирован", activated=True)

@auth_router.post("/login", response=LoginOutSchema)
async def login(request, payload:LoginInSchema) -> LoginOutSchema:
    user = await aauthenticate(
        request=request,
        username=payload.username,
        password=payload.password
    )
    if user is None:
        return LoginOutSchema(success=False, message="Неверный логин или пароль")

    return LoginOutSchema(
        success=True,
        message="Авторизация успешна",
        username=user.username,
        email=user.email,
        id=user.id,
        is_staff=user.is_staff
    )
