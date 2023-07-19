from django.db import models

class Criacao(models.Model):
    id = models.AutoField(primary_key=True)
    raca = models.CharField(max_length=30, verbose_name='raca')
    data_entrada = models.DateField(max_length=10, verbose_name='data_entrada')

    def __str__(self):
        return self.raca

    class Meta:
        ordering = ['data_entrada', 'raca']
        app_label = 'Producao'

class Coleta(models.Model):
    id = models.AutoField(primary_key=True)
    criacao = models.ForeignKey(Criacao, on_delete=models.CASCADE, verbose_name='criacao')
    data = models.DateField(max_length=10, verbose_name='data')
    quantidade = models.IntegerField(verbose_name='quantidade')

    class Meta:
        ordering = ['-data']