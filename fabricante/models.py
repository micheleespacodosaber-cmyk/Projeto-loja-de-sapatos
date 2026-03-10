from django.db import models

class Fabricante(models.Model):
    codigo = models.IntegerField()
    nome = models.CharField(max_length=70)