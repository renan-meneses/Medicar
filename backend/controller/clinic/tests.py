import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from .models import Specialty, Doctor, Agenda

@pytest.mark.django_db
class TestSpecialtyViewSet:

    def test_list_specialties(self):
        client = APIClient()
        url = reverse('specialty-list')
        response = client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == Specialty.objects.count()

@pytest.mark.django_db
class TestDoctorViewSet:

    def test_list_doctors(self):
        client = APIClient()
        url = reverse('doctor-list')
        response = client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == Doctor.objects.count()

@pytest.mark.django_db
class TestAgendaViewSet:

    def test_list_agendas(self):
        client = APIClient()
        url = reverse('agenda-list')
        response = client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == Agenda.objects.count()
