from django.db import models


class Receita(models.Model):
    descricao = models.CharField(max_length=50, blank=False)
    valor = models.DecimalField(max_digits=20, decimal_places=2, blank=False)
    data = models.DateField()

    def __str__(self):
        return self.descricao


class Despesa(models.Model):
    descricao = models.CharField(max_length=50, blank=False)
    valor = models.DecimalField(max_digits=20, decimal_places=2, blank=False)
    data = models.DateField()

    def __str__(self):
        return self.descricao
