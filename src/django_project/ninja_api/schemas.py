from datetime import datetime

from typing import Literal
from ninja import Schema, ModelSchema
from pydantic import EmailStr, Field, model_validator, ValidationError

from django_project.blog_app.models import Post, Category


class PostInSchema(ModelSchema):
    author_id: int
    topic_id: int
    class Meta:
        model = Post
        fields = ["title", "content",]


class PostOutSchema(ModelSchema):
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "content", "author", "topic", "published", "created_at"]

class CategoryInSchema(ModelSchema):
    class Meta:
        model = Category
        fields = ["title",]

class CategoryOutSchema(ModelSchema):
    class Meta:
        model = Category
        fields = ["id", "title", "slug"]


class FeedbackInSchema(Schema):
    name: str
    email: EmailStr
    message: str
    subject: Literal["Жалоба", "Благодарность", "Предложение", "Пожелание", "Прочее"]
    message: str


class FeedbackOutSchema(FeedbackInSchema):
    id: int
    created_at: datetime

class PostSearchOutSchema(Schema):
    id: int
    title: str
    slug: str
    headline: str
    rank: float
    published: bool

class RegisterInSchema(Schema):
    username: str = Field(min_length=3)
    email: EmailStr
    password: str
    password_confirm: str

    @model_validator(mode="after")
    def password_match(self) -> "RegisterInSchema":
        if self.password != self.password_confirm:
            raise ValidationError("Пароли не совпадают")
        return self

class RegisterOutSchema(Schema):
    message: str
    username: str
    email: EmailStr
    id: int

class ActivateOutSchema(Schema):
    message: str
    activated: bool

class LoginInSchema(Schema):
    username: str
    password: str

class LoginOutSchema(Schema):
    message: str
    success: bool
    username: str | None = None
    email: str | None = None
    id: int | None = None
    is_staff: bool
