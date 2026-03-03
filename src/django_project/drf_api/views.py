from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django_project.blog_app.management.commands import utils

from django_project.blog_app.models import Post, Category
from django_project.drf_api.permissions import IsAdminUserOrReadOnly, IsAuthorOrReadOnly
from django_project.drf_api.serializers import PostSerializer, CategorySerializer, FeedbackSerializer

from rest_framework import views


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = ["topic", "published"]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at"]

    def perform_create(self, serializer):
        title = serializer.validated_data["title"]
        slug = utils.translit_1(title)
        serializer.save(author=self.request.user, slug=slug)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields = ["title"]
    search_fields = ["title"]
    ordering_fields = ["title"]

    def perform_create(self, serializer):
        title = serializer.validated_data["title"]
        slug = utils.translit_1(title)
        serializer.save(slug=slug)

class FeedbackCreateAPIView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(name=self.request.user)

class FeedbackCreateSecondAPIView(views.APIView):
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        serializer.save(name=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
