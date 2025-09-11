# seu_app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Endereco

# Adicione esta linha para registrar o modelo Endereco, se ainda não estiver
admin.site.register(Endereco)

# Define o inline para o modelo Endereco
class EnderecoInline(admin.StackedInline):
    model = Endereco
    can_delete = False
    verbose_name_plural = 'Endereços'
    extra = 1   

# Define a nova classe UserAdmin para incluir o inline
class UserAdmin(BaseUserAdmin):
    inlines = (EnderecoInline,)

# Desregistra o UserAdmin padrão
admin.site.unregister(User)

# Registra a nova classe UserAdmin
admin.site.register(User, UserAdmin)


