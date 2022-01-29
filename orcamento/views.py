from rest_framework import viewsets
from orcamento.models import Receita, Despesa
from orcamento.serializer import ReceitaSerializer, DespesaSerializer


class ReceitasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as receitas"""

    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer


class DespesasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as despesas"""

    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
