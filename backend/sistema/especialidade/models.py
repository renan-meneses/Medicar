from django.db import models


class Especialidade(models.Model):
    nome = models.CharField(max_length=100)


def __unicode__(self):
    return self.nome

def __str__(self):
    return self.nome