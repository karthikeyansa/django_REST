from django.urls import path
from . import views

urlpatterns = [
    path('user/login/',views.login,name='login'),
    path('post/',views.Postview.as_view(),name='postview'),
    path('user/create/',views.Userview.as_view({'post':'create'}),name= 'usercreate'),
    path('user/list/',views.Userview.as_view({'get':'list'}),name='userslist'),
    path('user/find/<int:pk>',views.Userview.as_view({'get':'retrieve'}),name='finduser'),
    path('user/delete/<int:pk>',views.Userview.as_view({'get':'retrieve'}),name='deleteuser')
]