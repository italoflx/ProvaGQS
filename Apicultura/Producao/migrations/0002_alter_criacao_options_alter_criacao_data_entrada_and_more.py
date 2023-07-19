# Generated by Django 4.2.2 on 2023-07-19 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Producao', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='criacao',
            options={'ordering': ['data_entrada', 'raca']},
        ),
        migrations.AlterField(
            model_name='criacao',
            name='data_entrada',
            field=models.DateField(max_length=10, verbose_name='data_entrada'),
        ),
        migrations.AlterField(
            model_name='criacao',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='criacao',
            name='raca',
            field=models.CharField(max_length=30, verbose_name='raca'),
        ),
        migrations.CreateModel(
            name='Coleta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField(max_length=10, verbose_name='data')),
                ('quantidade', models.IntegerField(verbose_name='quantidade')),
                ('criacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Producao.criacao', verbose_name='criacao')),
            ],
        ),
    ]