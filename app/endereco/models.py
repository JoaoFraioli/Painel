from django.db import models
from django.contrib.auth.models import User


class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=255)
    cep = models.CharField(max_length=15, blank=True, null=True)
    numero = models.CharField(max_length=200, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    def __str__(self):
        return f'Endereço de {self.usuario.username}'