from django.db import models
from especialidade.models import Especialidade

class Medico(models.Model):
     nome = models.CharField(max_length=250)
     crm = models.CharField(max_length=50)
     email= models.EmailField(max_length=254,blank=True,)
     especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)


def __unicode__(self):
     return self.nome

def __str__(self):
      return self,nome