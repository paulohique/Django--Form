from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    telefone = models.IntegerField()
    numeroRifa = models.IntegerField()
    pago = models.BooleanField(default=False)
