from django.contrib import admin
from . import models

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id' , 'title', 'tier', 'type', 'language')

class FieldSubjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'semester', 'field', 'subject']

class ExaminationAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'week', 'subject']

admin.site.register(models.Subject, SubjectAdmin)
admin.site.register(models.FieldSubjects, FieldSubjectsAdmin)
admin.site.register(models.Examination, ExaminationAdmin)


