from django.shortcuts import render

from rest_framework import viewsets
from .serializers import PostSerializer, LikeSerializer, DislikeSerializer, CommentSerializer
from .serializers import CommentSerializer

from .models import Post, Comment,Like, Dislike

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('created')
    serializer_class =PostSerializer

class LikesViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all().order_by('created')
    serializer_class = LikeSerializer

class DislikesViewSet(viewsets.ModelViewSet):
    queryset = Dislike.objects.all().order_by('created')
    serializer_class = DislikeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('created')
    serializer_class = CommentSerializer
