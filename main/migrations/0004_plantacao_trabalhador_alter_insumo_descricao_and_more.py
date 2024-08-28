# Generated by Django 5.1 on 2024-08-28 05:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_insumo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plantacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('area_hectares', models.DecimalField(decimal_places=2, max_digits=10)),
                ('localizacao', models.CharField(max_length=255)),
                ('data_plantio', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Trabalhador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('funcao', models.CharField(max_length=100)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_admissao', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='insumo',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ControleInsumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_utilizada', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_uso', models.DateField()),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.insumo')),
                ('plantacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.plantacao')),
            ],
        ),
        migrations.CreateModel(
            name='Clima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_registro', models.DateField()),
                ('temperatura', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('umidade', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('precipitacao', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('plantacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.plantacao')),
            ],
        ),
        migrations.CreateModel(
            name='ProducaoEsperada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_sacas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_previsao', models.DateField()),
                ('plantacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.plantacao')),
            ],
        ),
        migrations.CreateModel(
            name='ProducaoRealizada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_sacas', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_colheita', models.DateField()),
                ('plantacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.plantacao')),
            ],
        ),
        migrations.CreateModel(
            name='ControleTrabalho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_trabalho', models.TextField()),
                ('horas_trabalhadas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data_trabalho', models.DateField()),
                ('plantacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.plantacao')),
                ('trabalhador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.trabalhador')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_vendida', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_venda', models.DateField()),
                ('comprador', models.CharField(max_length=255)),
                ('producao_realizada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.producaorealizada')),
            ],
        ),
    ]