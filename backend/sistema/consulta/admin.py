from django.contrib import admin
from .models import Agenda, Horario

class AgendaAdmin(admin.ModelAdmin):
   
    list_display = ('medico','dia')
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Horario)

