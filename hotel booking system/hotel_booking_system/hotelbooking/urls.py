from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('room/', views.room, name='room'),
    path('feature/', views.feature,name='feature'),
    path('menu/', views.menu,name='menu'),
    path('news/', views.news, name='news'),

]
