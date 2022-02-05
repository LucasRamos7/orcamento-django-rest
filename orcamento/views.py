from rest_framework import viewsets, generics, filters
from orcamento.models import Receita, Despesa
from orcamento.serializer import ReceitaSerializer, DespesaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum


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
    """Busca receitas pela descrição"""

    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_backends[1].search_param = 'descricao'
    search_fields = ['descricao']


class BuscaDespesas(generics.ListAPIView):
    """Busca despesas pela descrição"""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_backends[1].search_param = 'descricao'
    search_fields = ['descricao']


class ResumoView(APIView):

    def get(self, request, ano, mes):
        total_despesas = Despesa.objects.filter(data__year=ano, data__month=mes).aggregate(Sum('valor'))['valor__sum']
        total_receitas = Receita.objects.filter(data__year=ano, data__month=mes).aggregate(Sum('valor'))['valor__sum']
        despesa_por_categoria = Despesa.objects.filter(data__year=ano,
                                                       data__month=mes).values('categoria').annotate(Sum('valor'))
        saldo_final = total_receitas - total_despesas

        for despesa in despesa_por_categoria:
            despesa['valor'] = despesa['valor__sum']
            del despesa['valor__sum']

        return Response({
            'total_despesas': total_despesas,
            'total_receitas': total_receitas,
            'saldo_final': saldo_final,
            'despesa_por_categoria': despesa_por_categoria
        })
