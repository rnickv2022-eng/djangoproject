from django.contrib.postgres.search import SearchVector, SearchQuery, SearchHeadline, SearchRank
from django.http import HttpResponse
from ninja import NinjaAPI
from django_project.blog_app.management.commands import utils

from django_project.blog_app.models import Post, Category
from django_project.feedback_app.models import Feedback
from django_project.ninja_api.auth_routes import auth_router
from django_project.ninja_api.schemas import PostInSchema, PostOutSchema, FeedbackOutSchema, FeedbackInSchema, \
    PostSearchOutSchema, CategoryInSchema, CategoryOutSchema

router = NinjaAPI(
    version="1.0.0",
    title="Ninja API BLOG",
    description="Блог на Django Ninja API",
)
router.add_router("/auth", auth_router)

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

@router.get("/posts/search", response=list[PostSearchOutSchema])
async def search_posts(request, query: str, publ: bool | None=None) -> list[PostSearchOutSchema]:
    vector = SearchVector("title", weight="A", config="russian") + SearchVector("content", weight="B", config="russian") + SearchVector("topic__title", weight="C", config="russian")
    search_query = SearchQuery(query, config="russian")
    headline = SearchHeadline("content", search_query, config="russian", max_words=15, min_words=1)
    qs = Post.objects.annotate(rank=SearchRank(vector, search_query), headline=headline).filter(rank__gte=0.1).order_by("-rank")
    if publ is not None:
        qs = qs.filter(published=publ)
    results = [
        PostSearchOutSchema(
            id=post.pk,
            title=post.title,
            slug=post.slug,
            headline=post.headline,
            rank=post.rank,
            published=post.published
        )
        async for post in qs
    ]
    return results

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

@router.get("/categories", response=list[CategoryOutSchema])
async def categories_list(request, search_title: str | None=None, category_id: int | None=None) -> list[CategoryOutSchema]:
    qs = Category.objects.all()
    if search_title:
        qs = qs.filter(title__icontains=search_title)

    if category_id:
        qs = qs.filter(id=category_id)

    return [category async for category in qs]

@router.post("/categories", response=CategoryInSchema)
async def create_category(request, payload: CategoryInSchema) -> CategoryOutSchema:
    data = payload.model_dump()
    return await Category.objects.acreate(**data,slug=utils.translit_1(payload.title))

@router.get("/categories/{category_id}", response=CategoryOutSchema)
async def get_category(request, category_id:int) -> CategoryOutSchema | HttpResponse:
    try:
        category = await Category.objects.aget(pk=category_id)
        return category
    except Category.DoesNotExist:
        return router.create_response(request, {"detail": "Категория не найдена"}, status=404)

@router.post("/categories/{category_id}/delete")
async def delete_category(request, category_id:int) -> HttpResponse:
    if await Category.objects.filter(id=category_id).aexists():
        await Category.objects.filter(pk=category_id).adelete()
        return router.create_response(request, {"detail": "Категория удалена"},status=200)
    else:
        return router.create_response(request, {"detail": "Категория не найдена"}, status=404)
