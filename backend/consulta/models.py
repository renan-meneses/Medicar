from django.db import models
from medico.models import Medico

class Horario(models.Model):
    horario = models.TimeField()

def __str__(self):
        return self.horario


def __unicode__(self):
    return self.horario
class Consulta(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField(auto_now=False, auto_now_add=False)
    data_agendamento = models.DateTimeField( auto_now=True)
    horario = models.DateTimeField() 


def __unicode__(self):
       return self.horario
       return self.medico
       return self.dia
       return self.data_agendamento

def __str__(self):
        return self.horario
        return self.medico
        return self.dia
        return self.data_agendamento

class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField(auto_now=False, auto_now_add=False)
    horario = models.ManyToManyField(Horario)


def __unicode__(self):
     return self.horario
     return self.dia
     return self.medico


def __str__(self):
        return self.horario
        return self.dia
        return self.medico
