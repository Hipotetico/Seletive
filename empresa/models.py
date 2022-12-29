from django.db import models

# Create your models here.

class Empresa(models.Model):

    choices_nicho_mercado = (
        ('M', 'Mercado'),
        ('N', 'Nutrição'),
        ('D', 'Design')
    )
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    caracteristica_empresa = models.TextField()
    nicho_mercado = models.CharField(max_length=3, choices=choices_nicho_mercado)