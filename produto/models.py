from django.db import models

class Produto(models.Model):
    codigo = models.IntegerField()
    nome = models.CharField(max_length=70)
    preco_compra = models.FloatField()
    preco_venda = models.FloatField()
    cor = models.CharField(max_length=20)
    data_fabricacao = models.DateField()
    imagem = models.CharField(max_length=25)