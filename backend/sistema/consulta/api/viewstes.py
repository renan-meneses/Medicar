from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from consulta.models import Agenda, Horario, Consulta, Medico


class AgendaViewSet(viewsets.ModelViewSet):

    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    permission_classes = [permissions.IsAuthenticated]
