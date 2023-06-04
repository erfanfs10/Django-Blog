from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Post
from .serializer import PostSerializer


class PostView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        seri = PostSerializer(posts, many=True)
        return Response(seri.data)