from django.contrib import admin
from orcamento.models import Receita, Despesa


class Receitas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao', 'data')
    list_per_page = 20
    sortable_by = ('descricao', 'valor', 'data')


class Despesas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id', 'descricao')
    search_fields = ('descricao', 'data')
    list_per_page = 20
    sortable_by = ('descricao', 'valor', 'data')


admin.site.register(Receita, Receitas)
admin.site.register(Despesa, Despesas)
