from django.contrib import admin
from .models import Agenda

class AgendaAdmin(admin.ModelAdmin):
   
    list_display = ('medico','dia')
admin.site.register(Agenda, AgendaAdmin)
