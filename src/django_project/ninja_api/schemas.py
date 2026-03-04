from datetime import datetime

from typing import Literal
from ninja import Schema, ModelSchema
from pydantic import EmailStr

from django_project.blog_app.models import Post


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

class FeedbackInSchema(Schema):
    name: str
    email: EmailStr
    message: str
    subject: Literal["Жалоба", "Благодарность", "Предложение", "Пожелание", "Прочее"]
    message: str


class FeedbackOutSchema(FeedbackInSchema):
    id: int
    created_at: datetime
