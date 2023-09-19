from django.contrib import admin
from .models import Delegacia, Avaliacao, Regiao


@admin.register(Delegacia)
class DelegaciaAdmin(admin.ModelAdmin):
    list_filter = ('localizacao', 'titulo', 'url', 'criacao', 'atualizacao', 'ativo')
    ordering = ('localizacao',)
    search_fields = ('localizacao', 'titulo')


@admin.register(Regiao)
class RegiaoAdmin(admin.ModelAdmin):
    list_filter = ('cidade', 'cep', 'criacao', 'atualizacao', 'ativo')



@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_filter = ('delegacia', 'nome', 'comentario', 'avaliacao', 'criacao', 'atualizacao', 'ativo')
    ordering = ('delegacia',)
    search_fields = ('delegacia', 'nome')