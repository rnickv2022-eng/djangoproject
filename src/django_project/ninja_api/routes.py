from django.http import HttpResponse
from ninja import NinjaAPI
from django_project.blog_app.management.commands import utils

from django_project.blog_app.models import Post
from django_project.feedback_app.models import Feedback
from django_project.ninja_api.schemas import PostInSchema, PostOutSchema, FeedbackOutSchema, FeedbackInSchema

router = NinjaAPI(
    version="1.0.0",
    title="Ninja API BLOG",
    description="Блог на Django Ninja API",
)

@router.get("/ping")
def ping(request) -> dict[str, bool]:
    return {"pong":True}


@router.get("/posts", response=list[PostOutSchema])
async def posts_list(request, search: str | None=None, category_id: int | None=None) -> list[PostOutSchema]:
    qs = Post.objects.all()
    if search:
        qs = qs.filter(title__icontains=search)

    if category_id:
        qs = qs.filter(topic=category_id)

    return [post async for post in qs]

@router.get("/posts/{post_id}", response=PostOutSchema)
async def get_post(request, post_id:int) -> PostOutSchema | HttpResponse:
    try:
        post = await Post.objects.aget(pk=post_id)
        return post
    except Post.DoesNotExist:
        return router.create_response(request, {"detail":"Статья не найдена"}, status=404)

@router.post("/posts", response=PostOutSchema)
async def create_post(request, payload: PostInSchema) -> PostOutSchema:
    data = payload.model_dump()
    return await Post.objects.acreate(**data,slug=utils.translit_1(payload.title))

@router.post("/feedback", response=FeedbackOutSchema)
async def create_feedback(request, payload: FeedbackInSchema) -> FeedbackOutSchema:
    return await Feedback.objects.acreate(**payload.model_dump())
