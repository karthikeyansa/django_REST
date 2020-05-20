from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import PostSerializer,UserSerializer
from .models import Post


class Postview(APIView):
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

class Userview(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request,*args,**kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        try:
            user = User.objects.create_user(username, email, password)
            return Response({'message': 'User created successfully!!'}, status=200)
        except:
            return Response({'message': 'Sorry! The user already exsists'}, status=200)

    def list(self, request,*args,**kwargs):
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        user.delete()
        return Response(status=200)

def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user:
            return JsonResponse({'message':user},status=200)
        return JsonResponse({'message':'user not found'},status=200)
    return HttpResponse('method not allowed')
