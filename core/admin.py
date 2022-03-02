from django.contrib import admin

from .models import Filme, Avaliacao


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'filme', 'avaliacao', 'criacao', 'atualizacao', 'ativo')


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('filme', 'criacao', 'atualizacao', 'ativo')

