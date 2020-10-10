from django.db import models


class Especialidade(models.Model):
    nome = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



def __str__(self):
        return self.nome