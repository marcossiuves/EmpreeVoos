from django.contrib import admin
from .models import Destinos


# Register your models here.

@admin.register(Destinos)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nomeDestino','precoPorPessoa','descricao', 'slug']
