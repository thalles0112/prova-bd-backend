from django.db import models

# Create your models here.


class Venda(models.Model):
    bandejas = models.IntegerField()
    data = models.DateField()
    cliente = models.CharField(max_length=100)
    whatsapp = models.IntegerField()
    valor = models.FloatField()