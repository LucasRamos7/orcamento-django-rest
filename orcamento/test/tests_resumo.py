from rest_framework.test import APITestCase
from orcamento.models import Despesa, Receita
from django.urls import reverse
from rest_framework import status
from datetime import datetime


class ResumoTestCase(APITestCase):

    def setUp(self):
        self.receita_1 = Receita.objects.create(
            descricao='Receita Teste 1',
            valor='100',
            data=datetime.today()
        )
        self.despesa_1 = Despesa.objects.create(
            descricao='Despesa Teste 1',
            valor='100',
            data=self.receita_1.data,
            categoria='O'
        )

    def test_requisicao_get_para_listar_resumo_do_mes(self):
        """Teste para verificar a requisição GET que lista o resumo das despesas e receitas em um mês"""

        year = self.receita_1.data.year
        month = self.receita_1.data.month

        response = self.client.get(f'/resumo/{year}/{month}/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
