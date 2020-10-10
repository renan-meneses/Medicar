from django.db import models
from especialidade.models import Especialidade
from medico.models import Medico

class Consulta(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    Especialidade= models.ForeignKey(Medico, related_name='', on_delete=models.CASCADE)
    