from django.urls import path
from . import views
urlpatterns = [

    path('',views.Testview.as_view(),name='view'),

]