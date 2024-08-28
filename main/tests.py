import time
from random import randrange
from datetime import timedelta
from unittest.mock import patch

from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from .models import (
    Insumo,
    Plantacao,
    ControleInsumo,
    ProducaoEsperada,
    ProducaoRealizada,
    Clima,
    Trabalhador,
    ControleTrabalho,
    Venda,
    Usuario,
)
from .forms import RegistrarInsumoForm

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


class InsumoModelTest(TestCase):
    def setUp(self):
        self.insumo = Insumo.objects.create(
            nome="Insumo Teste", descricao="Descricao Teste", unidade_medida="kg"
        )

    def test_insumo_creation(self):
        self.assertEqual(self.insumo.nome, "Insumo Teste")
        self.assertEqual(self.insumo.descricao, "Descricao Teste")
        self.assertEqual(self.insumo.unidade_medida, "kg")

    def test_insumo_nome_max_length(self):
        max_length = self.insumo._meta.get_field("nome").max_length
        self.assertEqual(max_length, 100)

    def test_insumo_str_method(self):
        self.assertEqual(str(self.insumo), "Insumo Teste")


class RegistrarInsumoTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("registrar_insumo")

    def test_registrar_insumo_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/registrar_insumo.html")
        self.assertIsInstance(response.context["form"], RegistrarInsumoForm)

    @patch('main.views.pd.DataFrame', return_value=pd.DataFrame({
        'Data Esperada': ['2023-08-28'],
        'Quantidade de Sacas': [10]
    }))
    def test_registrar_insumo_post_valid(self, MockFramework):
        data = {
            "nome": "Insumo Teste",
            "descricao": "Descrição Teste",
            "unidade_medida": "kg"
        }
        response = self.client.post(reverse("registrar_insumo"), data)
        self.assertEqual(response.status_code, 302)  # Verifica redirecionamento
        self.assertTrue(Insumo.objects.filter(nome="Insumo Teste").exists())
        
    def test_registrar_insumo_post_invalid(self):
        data = {"nome": "", "descricao": "", "unidade_medida": ""}  # Dados inválidos
        response = self.client.post(reverse("registrar_insumo"), data)
        self.assertEqual(
            response.status_code, 200
        )  # Verifica que a página de formulário é renderizada
        self.assertTemplateUsed(response, "main/registrar_insumo.html")


class UsuarioModelTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nome="Teste Usuario",
            email="teste@usuario.com",
            cpf="12345678901",
            senha="senha123",
        )

    def test_usuario_creation(self):
        self.assertEqual(self.usuario.nome, "Teste Usuario")
        self.assertEqual(self.usuario.email, "teste@usuario.com")
        self.assertEqual(self.usuario.cpf, "12345678901")
        self.assertTrue(self.usuario.senha)

    def test_usuario_nome_max_length(self):
        max_length = self.usuario._meta.get_field("nome").max_length
        self.assertEqual(max_length, 80)

    def test_usuario_email_unique(self):
        with self.assertRaises(ValidationError):
            Usuario.objects.create(
                nome="Outro Usuario",
                email="teste@usuario.com",
                cpf="09876543210",
                senha="senha123",
            )
            # A validação manual deve ser chamada antes de salvar
            self.usuario.full_clean()  # Este método irá disparar o ValidationError
            self.usuario.save()  # Este save não será alcançado se o ValidationError for disparado

    def test_usuario_cpf_length(self):
        max_length = self.usuario._meta.get_field("cpf").max_length
        self.assertEqual(max_length, 11)


class PlantacaoModelTest(TestCase):
    def setUp(self):
        self.plantacao = Plantacao.objects.create(
            nome="Plantacao Teste",
            area_hectares=10.5,
            localizacao="Local Teste",
            data_plantio="2023-01-01",
        )

    def test_plantacao_creation(self):
        self.assertEqual(self.plantacao.nome, "Plantacao Teste")
        self.assertEqual(self.plantacao.area_hectares, 10.5)
        self.assertEqual(self.plantacao.localizacao, "Local Teste")
        self.assertEqual(self.plantacao.data_plantio, "2023-01-01")

    def test_plantacao_nome_max_length(self):
        max_length = self.plantacao._meta.get_field("nome").max_length
        self.assertEqual(max_length, 100)

    def test_plantacao_str_method(self):
        self.assertEqual(str(self.plantacao), "Plantacao Teste")


class DashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("dashboard")
        self.plantacao = Plantacao.objects.create(
            nome="Plantacao Teste",
            area_hectares=10.5,
            localizacao="Local Teste",
            data_plantio="2023-01-01",
        )
        self.insumo = Insumo.objects.create(
            nome="Insumo Teste", descricao="Descricao Teste", unidade_medida="kg"
        )
        self.controle_insumo = ControleInsumo.objects.create(
            plantacao=self.plantacao,
            insumo=self.insumo,
            quantidade_utilizada=100,
            data_uso="2023-01-01",
        )
        self.producao_esperada = ProducaoEsperada.objects.create(
            plantacao=self.plantacao, quantidade_sacas=50, data_previsao="2023-12-01"
        )
        self.producao_realizada = ProducaoRealizada.objects.create(
            plantacao=self.plantacao, quantidade_sacas=45, data_colheita="2023-11-01"
        )
        self.clima = Clima.objects.create(
            plantacao=self.plantacao,
            data_registro="2023-01-01",
            temperatura=25,
            umidade=80,
        )
        self.trabalhador = Trabalhador.objects.create(
            nome="Trabalhador Teste",
            funcao="Colheita",
            salario=1320,
            data_admissao="2023-01-01",
        )
        self.controle_trabalho = ControleTrabalho.objects.create(
            trabalhador=self.trabalhador,
            plantacao=self.plantacao,
            horas_trabalhadas=8,
            data_trabalho="2023-01-01",
        )
        self.venda = Venda.objects.create(
            producao_realizada=self.producao_realizada,
            quantidade_vendida=5,
            preco_unitario=98,
            data_venda="2023-12-15",
            comprador="Comprador Teste",
        )

    def test_dashboard_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "main/dashboard.html")
        self.assertEqual(len(response.context["plantacoes"]), 1)
        self.assertEqual(len(response.context["insumos"]), 1)
        self.assertEqual(len(response.context["controles_insumos"]), 1)
        self.assertEqual(len(response.context["producoes_esperadas"]), 1)
        self.assertEqual(len(response.context["producoes_realizadas"]), 1)
        self.assertEqual(len(response.context["climas"]), 1)
        self.assertEqual(len(response.context["trabalhadores"]), 1)
        self.assertEqual(len(response.context["controles_trabalhos"]), 1)
        self.assertEqual(len(response.context["vendas"]), 1)
        self.assertIn("grafico", response.context)


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


class SeleniumTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()


class SystemTests(SeleniumTestCase):
    def test_authentication_form(self):
        usuario = Usuario(nome="Gabriel", email="g@gmail.com", senha="123456")
        usuario.save()

        # Go to the login page
        self.driver.get(self.live_server_url + "/login")

        # Find HTML elements
        email_input = self.driver.find_element(By.ID, "id_email")
        password_input = self.driver.find_element(By.ID, "id_senha")

        email_input.send_keys("g@gmail.com")
        time.sleep(2)
        password_input.send_keys("123456")
        time.sleep(2)
        login_button = self.driver.find_element(By.CLASS_NAME, "submit-btn")

        login_button.click()

        time.sleep(3)
        self.assertEqual(self.driver.current_url, self.live_server_url + "/dashboard")

    def test_register_insumo(self):
        # Go to the dashboard page
        self.driver.get(self.live_server_url + "/dashboard")
        link_insumos = self.driver.find_element(
            By.CSS_SELECTOR, 'a[data-target="#insumos-section"]'
        )
        link_insumos.click()
        time.sleep(1)
        bnt_registrar = self.driver.find_element(By.CSS_SELECTOR, ".submit-btn a")
        bnt_registrar.click()

        nome_input = self.driver.find_element(By.ID, "id_nome")
        descricao_input = self.driver.find_element(By.ID, "id_descricao")
        unidade_input = self.driver.find_element(By.ID, "id_unidade_medida")

        nome_input.send_keys("NPK")
        descricao_input.send_keys(
            "Fonte de Nitrogenio, Fosforo, e Potassio ( um adubo generico que tem os 3 nutrientes)"
        )
        unidade_input.send_keys("kg")
        btn_submit = self.driver.find_element(By.CSS_SELECTOR, "button.submit-btn")
        time.sleep(2)
        btn_submit.click()

        link_insumos = self.driver.find_element(
            By.CSS_SELECTOR, 'a[data-target="#insumos-section"]'
        )
        link_insumos.click()

        insumo = list(
            map(
                lambda x: x.text,
                self.driver.find_elements(
                    By.CSS_SELECTOR, "div#insumos-section table tbody tr td"
                ),
            )
        )

        self.assertEqual(insumo[0], "NPK")
        self.assertEqual(
            insumo[1],
            "Fonte de Nitrogenio, Fosforo, e Potassio ( um adubo generico que tem os 3 nutrientes)",
        )
        self.assertEqual(insumo[2], "kg")
        time.sleep(2)
