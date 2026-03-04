from rest_framework import serializers
from django_project.blog_app.models import Post, Category
from django_project.feedback_app.models import Feedback


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "slug", "content", "author", "published", "created_at", "topic")
        read_only_fields = ("slug", "author")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title", "slug")
        read_only_fields = ("slug",)

class FeedbackSerializer(serializers.Serializer):
    subject = serializers.CharField()
    email = serializers.EmailField()
    message = serializers.CharField()

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)
