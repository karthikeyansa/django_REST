from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post

class Testview(APIView):
    def get(self, request, *args, **kwargs):
        queries = Post.objects.all()
        serializer =PostSerializer(queries,many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
