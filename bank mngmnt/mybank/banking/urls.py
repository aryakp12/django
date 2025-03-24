from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/<int:account_id>/', views.account_detail, name='account_detail'),
    path('transfer/', views.transfer, name='transfer'),
]