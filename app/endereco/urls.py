from django.urls import path
from .views import EnderecoListAPIView

urlpatterns = [
    path('enderecos/', EnderecoListAPIView.as_view(), name='endereco-list'),
]
