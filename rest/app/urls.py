from django.urls import path,include
from . import views
from rest_framework import routers

users = routers.DefaultRouter()
users.register('users',views.Userview)

posts = routers.DefaultRouter()
users.register('posts',views.Postview)

urlpatterns = [
    path('',include(users.urls)),
    path('',include(posts.urls)),
    path('user/login/',views.login,name='login'),
]
#   path('post/',views.Postview.as_view(),name='postview'),
#   path('user/create/',views.Userview.as_view({'post':'create'}),name= 'usercreate'),
#   path('user/list/',views.Userview.as_view({'get':'list'}),name='userslist'),
#   path('user/find/<int:pk>',views.Userview.as_view({'get':'retrieve'}),name='finduser'),
#   path('user/delete/<int:pk>',views.Userview.as_view({'get':'destroy'}),name='deleteuser')
#'get': 'list',
#'post': 'create'
#'get': 'retrieve',
#'put': 'update',
#'patch': 'partial_update',
#'delete': 'destroy'