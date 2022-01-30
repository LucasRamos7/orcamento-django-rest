from rest_framework import viewsets, generics
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


class ListaReceitasMes(generics.ListAPIView):
    """Exibindo todas as receitas de um determinado mês"""

    def get_queryset(self):

        queryset = Receita.objects.filter(data__year=self.kwargs['ano'], data__month=self.kwargs['mes'])
        return queryset

    serializer_class = ReceitaSerializer


class ListaDespesasMes(generics.ListAPIView):
    """Exibindo todas as despesas de um determinado mês"""

    def get_queryset(self):

        queryset = Despesa.objects.filter(data__year=self.kwargs['ano'], data__month=self.kwargs['mes'])
        return queryset

    serializer_class = DespesaSerializer
