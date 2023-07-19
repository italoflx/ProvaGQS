from django import forms
from django.forms import ModelForm
from datetime import date, timedelta
from Producao.models import Coleta, Criacao


class ColetaForm(ModelForm):
    class Meta:
        model = Coleta
        fields = ['criacao', 'data', 'quantidade']

    def clean_data(self):
        data = self.cleaned_data['data']
        if data > date.today():
            raise forms.ValidationError("A data não pode ser futura.")
        return data

    def clean_nome(self):
        cleaned_data = super().clean()

        criacao = self.cleaned_data['criacao']
        data = self.cleaned_data['data']
        quantidade = self.cleaned_data['quantidade']

        coletas_existentes = Coleta.objects.filter(criacao=criacao, data=data, quantidade=quantidade)


class CriacaoForm(ModelForm):
    class Meta:
        model = Criacao
        fields = ['raca', 'data_entrada']

    def clean_data_entrada(self):
        data_entrada = self.cleaned_data['data_entrada']
        if data_entrada > date.today():
            raise forms.ValidationError("A data de entrada não pode ser futura.")
        return data_entrada
