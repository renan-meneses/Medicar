from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from medico.models import Medico
from .serializer import MedicoSerializer

class MedicoViewSet(viewsets.ModelViewSet):

    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    # permission_classes = [permissions.IsAuthenticated]


