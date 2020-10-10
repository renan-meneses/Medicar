from django.contrib import admin

from .models import Especialidade


class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'create_at')
admin.site.register(Especialidade, EspecialidadeAdmin)