from django.db import models

class Contador(models.Model):
    valor = models.CharField(max_length=255, unique=True)
    contagem = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.valor} - {self.contagem}"
