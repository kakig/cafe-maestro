from django.db import models

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=80)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    senha = models.CharField(max_length=20)
