# Generated by Django 5.1 on 2024-08-11 22:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("clinic", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="medicalappointment",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_medical_appointment",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Paciente",
            ),
        ),
        migrations.AddField(
            model_name="doctor",
            name="specialty",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="doctor",
                to="clinic.specialty",
                verbose_name="Especialidade",
            ),
        ),
    ]
