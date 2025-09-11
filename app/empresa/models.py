from django.db import models
from django.contrib.auth import get_user_model

class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='empresas')
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, help_text='Logo da empresa (JPEG/PNG)')

    def __str__(self):
        return self.nome
