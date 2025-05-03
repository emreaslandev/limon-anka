from django.urls import path
from . import views


urlpatterns = [

    path('', views.testimonial, name='testimonials'),



]

