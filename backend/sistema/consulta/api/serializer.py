from rest_framework import serializers
from consulta.models import Agenda, Horario, Consulta


class AgendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medico
        fields = ['id', 'medico', 'data', 'horarios']


class HorarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medico
        fields = ['id',horario]

class AgendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medico
        fields = ['id', 'medico', 'data', 'horarios']
