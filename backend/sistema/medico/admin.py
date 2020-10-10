from django.contrib import admin
from .models import Medico

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('name', 'crm')
admin.site.register(Medico,MedicoAdmin)