from datetime import timezone, timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
from Producao.forms import CriacaoForm, ColetaForm
from Producao.models import Coleta, Criacao

class TestFormsAndModels(TestCase):
    def setUp(self):
        self.criacao1 = Criacao.objects.create(raca='Abelha X', data_entrada='2023-06-01')

        coleta_existente = Coleta.objects.create(
            criacao=self.criacao1,
            data='2023-01-01',
            quantidade=10
        )

    def test_tamanho_maximo_caracteres(self):
        # Verificar o tamanho máximo do campo "raca" na model Criacao
        max_length_raca = Criacao._meta.get_field('raca').max_length
        criacao = Criacao.objects.create(raca='A' * max_length_raca, data_entrada='2023-06-01')
        self.assertEqual(len(criacao.raca), max_length_raca)

    def test_elementos_obrigatorios(self):
        # Testar se o campo "raca" na model Criacao é obrigatório
        with self.assertRaises(ValidationError):
            criacao = Criacao.objects.create(data_entrada='2023-06-01')
            criacao.full_clean()

        # Testar se o campo "quantidade" na model Coleta é obrigatório
        criacao = Criacao.objects.create(raca='Abelha X', data_entrada='2023-06-01')
        with self.assertRaises(ValidationError):
            coleta = Coleta(criacao=criacao, data='2023-06-01')
            coleta.full_clean()

    def test_verbose_name(self):
        # Verificar o verbose_name do campo "raca" na model Criacao
        verbose_name_raca = Criacao._meta.get_field('raca').verbose_name
        self.assertEqual(verbose_name_raca, 'raca')

    def test_ordem_coletas(self):
        criacao = Criacao.objects.create(raca='Abelha X', data_entrada='2023-06-01')

        coleta1 = Coleta.objects.create(criacao=criacao, data='2023-06-02', quantidade=10)
        coleta2 = Coleta.objects.create(criacao=criacao, data='2023-06-01', quantidade=15)
        coleta3 = Coleta.objects.create(criacao=criacao, data='2023-06-03', quantidade=5)

        coletas = Coleta.objects.all()
        self.assertEqual(coletas[0], coleta3)
        self.assertEqual(coletas[1], coleta1)
        self.assertEqual(coletas[2], coleta2)