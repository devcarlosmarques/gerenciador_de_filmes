from django.db import models

class Filme(models.Model):
    nome = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    sinopse = models.TextField(max_length=255)

    def __str__(self):
        return self.nome