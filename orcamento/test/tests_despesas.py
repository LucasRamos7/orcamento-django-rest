from rest_framework.test import APITestCase
from orcamento.models import Despesa
from django.urls import reverse
from rest_framework import status
from datetime import datetime


class DespesaTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Despesas-list')
        self.despesa_1 = Despesa.objects.create(
            descricao='Despesa Teste 1',
            valor='100',
            data=datetime.today(),
            categoria='O'
        )

    def test_requisicao_get_para_listar_todas_as_despesas(self):
        """Teste para verificar a requisição GET que lista todas as despesas"""

        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_uma_despesa(self):
        """Teste para verificar a requisição GET que lista uma única despesa"""

        id_despesa = self.despesa_1.id

        response = self.client.get(f'/despesas/{id_despesa}/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_despesas_do_mes(self):
        """Teste para verificar a requisição GET que lista todas as despesas de um mês"""

        year = self.despesa_1.data.year
        month = self.despesa_1.data.month
        response = self.client.get(f'/despesas/{year}/{month}/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_buscar_despesa_por_descricao(self):
        """Teste para verificar a requisição GET que busca as despesas por sua descrição"""

        descricao = self.despesa_1.descricao
        response = self.client.get(f'/receitas/?descricao={descricao}/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_despesa(self):
        """Teste para verificar a requisição POST que cria uma nova despesa"""

        data = {
            'descricao': 'Despesa Teste 2',
            'valor': '150',
            'data': '2022-02-09',
            'categoria': 'A'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_post_exige_todos_os_campos_para_criar_despesa(self):
        """Teste para verificar se a requisição POST exige que todos os campos estejam preenchidos para criar despesa"""

        data = {
            'descricao': 'Despesa Teste 2',

            'data': '2022-02-09'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_requisicao_post_nao_permite_despesas_com_descricao_repetida_no_mesmo_mes(self):
        """Teste para verificar se a requisição POST proíbe que duas despesas com a mesma descrição sejam cadastradas
        no mesmo mês"""

        data = {
            'descricao': self.despesa_1.descricao,
            'valor': '150',
            'data': '2022-02-09'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_requisicao_put_para_atualizar_despesa(self):
        """Teste para verificar a requisição PUT que atualiza uma despesa"""

        id_despesa = self.despesa_1.id
        data = {
            'descricao': 'Despesa Teste 1 atualizada',
            'valor': '100',
            'data': '2022-02-09',
            'categoria': 'A'
        }

        response = self.client.put(f'/despesas/{id_despesa}/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete_para_apagar_despesa(self):
        """Teste para verificar a requisição DELETE que apaga uma despesa"""

        id_despesa = self.despesa_1.id

        response = self.client.delete(f'/despesas/{id_despesa}/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
