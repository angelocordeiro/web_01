from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    periodo_ingresso = models.CharField(max_length=10)
    nota_web = models.DecimalField(max_digits=5, decimal_places=2)
    situacao = models.CharField(max_length=20)

    def __str__(self):
        return self.nome