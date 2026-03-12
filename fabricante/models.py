from django.db import models

class Fabricante(models.Model):
    codigo = models.IntegerField()
    nome = models.CharField(max_length=70)

class ContatoSac(models.Model):
    nome_completo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    melhor_hora_contato = models.CharField(max_length=10)
    mensagem = models.CharField(max_length=1024)