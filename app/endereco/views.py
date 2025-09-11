from rest_framework.generics import ListCreateAPIView
from endereco.serializers import EnderecoSerializer
from .models import Endereco

class EnderecoListAPIView(ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer