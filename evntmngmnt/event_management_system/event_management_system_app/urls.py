from django.urls import path
from event_management_system_app import views

urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('categories/', views.category_list, name='category_list'),
]
