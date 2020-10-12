from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from especialidade.models import Especialidade
from .serializer import EspecialidadeSerializer

class EspecialidadeViewSet(viewsets.ModelViewSet):

    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    permission_classes = [permissions.IsAuthenticated]


