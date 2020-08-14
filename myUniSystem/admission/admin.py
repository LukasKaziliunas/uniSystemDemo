from django.contrib import admin
from . import models

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name')

class FieldAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'area_id', 'code']


admin.site.register(models.Area, AreaAdmin)
admin.site.register(models.Field, FieldAdmin)