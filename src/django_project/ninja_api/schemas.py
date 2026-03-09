from datetime import datetime

from typing import Literal
from ninja import Schema, ModelSchema
from pydantic import EmailStr

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
