# usuarios/urls.py
from django.urls import path
from .views import UserListCreateAPIView

urlpatterns = [
    path('api/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/', UserListCreateAPIView.as_view(), name='user-list-create'),
]