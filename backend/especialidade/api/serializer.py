from rest_framework import serializers
from especialidade.models import Especialidade
class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__'