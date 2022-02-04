from rest_framework import viewsets, generics, filters
from rest_framework.filters import SearchFilter
from orcamento.models import Receita, Despesa
from orcamento.serializer import ReceitaSerializer, DespesaSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ReceitasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as receitas"""

    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_param = ['descricao']
    search_fields = ['descricao']


class DespesasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as despesas"""

    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['descricao']


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


class BuscaReceitas(generics.ListAPIView):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_backends[1].search_param = 'descricao'
    search_fields = ['descricao']


class BuscaDespesas(generics.ListAPIView):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_backends[1].search_param = 'descricao'
    search_fields = ['descricao']

