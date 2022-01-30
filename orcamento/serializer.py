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
    class Meta:
        model = Despesa
        fields = ['id', 'descricao', 'valor', 'data', 'categoria']

        validators = [
            UniqueForMonthValidator(
                queryset=Despesa.objects.all(),
                field='descricao',
                date_field='data'
            )
        ]
