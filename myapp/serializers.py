from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'description', 'image', 'user', 'Likes', 'Dislikes')