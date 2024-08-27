from django.db import models

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=80)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    senha = models.CharField(max_length=20)


class Plantacao(models.Model):
    nome = models.CharField(max_length=100)
    area_hectares = models.DecimalField(max_digits=10, decimal_places=2)
    localizacao = models.CharField(max_length=255)
    data_plantio = models.DateField()

    def __str__(self):
        return self.nome


class Insumo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    unidade_medida = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class ControleInsumo(models.Model):
    plantacao = models.ForeignKey(Plantacao, on_delete=models.CASCADE)
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    quantidade_utilizada = models.DecimalField(max_digits=10, decimal_places=2)
    data_uso = models.DateField()

    def __str__(self):
        return f'{self.plantacao} - {self.insumo}'


class ProducaoEsperada(models.Model):
    plantacao = models.ForeignKey(Plantacao, on_delete=models.CASCADE)
    quantidade_sacas = models.DecimalField(max_digits=10, decimal_places=2)
    data_previsao = models.DateField()

    def __str__(self):
        return f'{self.plantacao} - {self.quantidade_sacas} sacas esperadas'


class ProducaoRealizada(models.Model):
    plantacao = models.ForeignKey(Plantacao, on_delete=models.CASCADE)
    quantidade_sacas = models.DecimalField(max_digits=10, decimal_places=2)
    data_colheita = models.DateField()

    def __str__(self):
        return f'{self.plantacao} - {self.quantidade_sacas} sacas colhidas'


class Clima(models.Model):
    plantacao = models.ForeignKey(Plantacao, on_delete=models.CASCADE)
    data_registro = models.DateField()
    temperatura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    umidade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    precipitacao = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'Clima em {self.plantacao} em {self.data_registro}'


class Trabalhador(models.Model):
    nome = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_admissao = models.DateField()

    def __str__(self):
        return self.nome


class ControleTrabalho(models.Model):
    trabalhador = models.ForeignKey(Trabalhador, on_delete=models.CASCADE)
    plantacao = models.ForeignKey(Plantacao, on_delete=models.CASCADE)
    descricao_trabalho = models.TextField()
    horas_trabalhadas = models.DecimalField(max_digits=5, decimal_places=2)
    data_trabalho = models.DateField()

    def __str__(self):
        return f'{self.trabalhador} em {self.plantacao} - {self.data_trabalho}'


class Venda(models.Model):
    producao_realizada = models.ForeignKey(ProducaoRealizada, on_delete=models.CASCADE)
    quantidade_vendida = models.DecimalField(max_digits=10, decimal_places=2)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateField()
    comprador = models.CharField(max_length=255)

    def __str__(self):
        return f'Venda para {self.comprador} - {self.quantidade_vendida} sacas'