from django.contrib import admin
from . import models


class StudentAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'code', 'studyGroup')


class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'field']


class StudentSubjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'subject', 'semester']


class StudentExaminations(admin.ModelAdmin):
    list_display = ['id', 'grade', 'studentSubject', 'examination']


class GroupSubjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'semester', 'professor', 'study_group', 'subject']


admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.StudentSubjects, StudentSubjectsAdmin)
admin.site.register(models.StudyGroup, StudyGroupAdmin)
admin.site.register(models.StudentExaminations, StudentExaminations)
admin.site.register(models.GroupSubjects, GroupSubjectsAdmin)