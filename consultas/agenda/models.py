from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=40)
    rua = models.CharField(max_length=40)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=40)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


