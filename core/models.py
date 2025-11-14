# core/models.py
from django.db import models

class Receita(models.Model):
    nome = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()

    def __str__(self):
        return self.nome