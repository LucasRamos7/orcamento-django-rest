from rest_framework import serializers
from rest_framework.validators import UniqueForMonthValidator
from orcamento.models import Receita, Despesa


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['id', 'descricao', 'valor', 'data']

        validators = [
            UniqueForMonthValidator(
                queryset=Receita.objects.all(),
                field='descricao',
                date_field='data'
            )
        ]


class DespesaSerializer(serializers.ModelSerializer):
    nome_categoria = serializers.SerializerMethodField()

    class Meta:
        model = Despesa
        fields = ['id', 'descricao', 'valor', 'data', 'nome_categoria']

        validators = [
            UniqueForMonthValidator(
                queryset=Despesa.objects.all(),
                field='descricao',
                date_field='data'
            )
        ]

    def get_nome_categoria(self, obj):
        return obj.get_categoria_display()
