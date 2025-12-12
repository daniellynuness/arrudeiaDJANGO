from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'cpf', 'telefone', 'data_criacao')
    list_filter = ('data_criacao',)
    search_fields = ('user__email', 'cpf', 'telefone')
    readonly_fields = ('data_criacao',)
