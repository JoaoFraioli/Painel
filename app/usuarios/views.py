# usuarios/views.py
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer

# READ - Listar todos os usuários
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

# CREATE - API de Registro de Usuário
class UserListCreateAPIView(generics.ListCreateAPIView): # <-- New View
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]