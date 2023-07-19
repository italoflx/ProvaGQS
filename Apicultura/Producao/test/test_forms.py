from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from Producao.forms import CriacaoForm, ColetaForm
from Producao.models import Coleta, Criacao


class TestCriacaoForm(TestCase):
    def setUp(self):
        self.criacao1 = Criacao.objects.create(raca='Abelha X', data_entrada='2023-06-01')

        coleta_existente = Coleta.objects.create(
            criacao=self.criacao1,
            data='2023-01-01',
            quantidade=10
        )

    def test_data_entrada_futura(self):
        data_futura = timezone.now().date() + timedelta(days=1)
        form_data = {
            'raca': 'Abelha X',
            'data_entrada': data_futura,
        }
        form = CriacaoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('data_entrada', form.errors)

    def test_data_entrada_passada(self):
        data_passada = timezone.now().date() - timedelta(days=1)
        form_data = {
            'raca': 'Abelha X',
            'data_entrada': data_passada,
        }
        form = CriacaoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_coleta_existente(self):
        form_data = {
            'criacao': self.criacao1.pk,
            'data': '2023-01-01',
            'quantidade': 10,
        }
        form = ColetaForm(data=form_data)
        self.assertTrue(form.is_valid())

class TestColetaForm(TestCase):
    def setUp(self):
        # Crie uma Criacao para ser usada nos testes
        self.criacao1 = Criacao.objects.create(raca='Abelha X', data_entrada='2023-06-01')

        # Crie uma Coleta existente com os mesmos valores
        coleta_existente = Coleta.objects.create(
            criacao=self.criacao1,
            data='2023-01-01',
            quantidade=10
        )

    def test_coleta_existente(self):
        form_data = {
            'criacao': self.criacao1.pk,
            'data': '2023-01-01',
            'quantidade': 10,
        }
        form = ColetaForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_data_futura(self):
        data_futura = timezone.now().date() + timedelta(days=1)
        form_data = {
            'criacao': self.criacao1.pk,
            'data': data_futura,
            'quantidade': 10,
        }
        form = ColetaForm(data=form_data)
        self.assertFalse(form.is_valid())

    # def test_data_passada(self):
    #     data_passada = timezone.now().date() - timedelta(days=1)
    #     form_data = {
    #         'criacao': self.criacao1.pk,
    #         'data': data_passada,
    #         'quantidade': 10,
    #     }
    #     form = ColetaForm(data=form_data)
    #     self.assertTrue(form.is_valid())