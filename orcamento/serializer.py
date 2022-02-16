from rest_framework import serializers
from rest_framework.validators import UniqueForMonthValidator, UniqueTogetherValidator
from orcamento.models import Receita, Despesa
from django.contrib.auth.models import User


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


class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['username', 'password']
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username']
            )
        ]

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response.pop('password')
        return response
