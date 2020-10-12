from rest_framework import serializers
from medico.models import Medico
from especialidade.models import Especialidade
class MedicoSerializer(serializers.ModelSerializer):
    # especialidade = serializers.StringRelatedField(many=True)
    class Meta:
        model = Medico
        fields = ['id', 'nome', 'crm', 'especialidade']
