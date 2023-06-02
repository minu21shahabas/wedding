from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
   path('',views.home,name='home'),
   path('about',views.about,name='about'),
   path('homepage',views.homepage,name='homepage'),
   path('gallery',views.gallery,name='gallery'),
   path('con',views.con,name='con'),
]