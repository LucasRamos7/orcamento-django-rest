from rest_framework.test import APITestCase
from orcamento.models import Receita
from django.urls import reverse
from rest_framework import status
from datetime import datetime


class ReceitaTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Receitas-list')
        self.receita_1 = Receita.objects.create(descricao='Receita Teste 1', valor='100', data=datetime.today())

    def test_requisicao_get_para_listar_todas_as_receitas(self):
        """Teste para verificar a requisição GET que lista todas as receitas"""

        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_uma_receita(self):
        """Teste para verificar a requisição GET que lista uma única receita"""

        id_receita = self.receita_1.id

        response = self.client.get(f'/receitas/{id_receita}')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_receitas_do_mes(self):
        """Teste para verificar a requisição GET que lista todas as receitas de um mês"""

        year = self.receita_1.data.year
        month = self.receita_1.data.month
        response = self.client.get(f'/receitas/{year}/{month}/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_buscar_receita_por_descricao(self):
        """Teste para verificar a requisição GET que busca as receitas por sua descrição"""

        descricao = self.receita_1.descricao
        response = self.client.get(f'/receitas/?descricao={descricao}/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_receita(self):
        """Teste para verificar a requisição POST que cria uma nova receita"""

        data = {
            'descricao': 'Receita Teste 2',
            'valor': '150',
            'data': '2022-02-09'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_post_exige_todos_os_campos_para_criar_receita(self):
        """Teste para verificar se a requisição POST exige que todos os campos estejam preenchidos para criar receita"""

        data = {
            'descricao': 'Receita Teste 2',

            'data': '2022-02-09'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_requisicao_post_nao_permite_receitas_com_descricao_repetida_no_mesmo_mes(self):
        """Teste para verificar se a requisição POST proíbe que duas receitas com a mesma descrição sejam cadastradas
        no mesmo mês"""

        data = {
            'descricao': self.receita_1.descricao,
            'valor': '150',
            'data': '2022-02-09'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_requisicao_put_para_atualizar_receita(self):
        """Teste para verificar a requisição PUT que atualiza uma receita"""

        id_receita = self.receita_1.id
        data = {
            'descricao': 'Receita Teste 1 atualizada',
            'valor': '100',
            'data': '2022-02-09'
        }

        response = self.client.put(f'/receitas/{id_receita}/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete_para_apagar_receita(self):
        """Teste para verificar a requisição DELETE que apaga uma receita"""

        id_receita = self.receita_1.id

        response = self.client.delete(f'/receitas/{id_receita}/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
