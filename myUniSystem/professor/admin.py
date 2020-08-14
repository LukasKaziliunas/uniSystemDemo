from django.contrib import admin
from . import models

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('account_id' , 'phone', 'code')


admin.site.register(models.Professor, ProfessorAdmin)
