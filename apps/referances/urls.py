from django.urls import path
from . import views


urlpatterns = [

    path('', views.referance_list, name='referance_list'),
    path('<slug:slug>/', views.referance_detail, name='referance_detail'),



]
