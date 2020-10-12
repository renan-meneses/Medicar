from rest_framework import serializers
from consulta.models import Agenda, Horario, Consulta


class AgendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agenda
        fields = ['id', 'medico.nome', 'data', 'horarios']


class HorarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Horario
        fields = ['id','horario']

class AgendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consulta
        fields = ['id', 'medico', 'data', 'horarios']
