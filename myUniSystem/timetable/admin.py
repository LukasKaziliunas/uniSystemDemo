from django.contrib import admin
from . import models


class TimeAdmin(admin.ModelAdmin):
    list_display = ('begins', 'ends')


class TimetableAdmin(admin.ModelAdmin):
    list_display = ('subject', 'weekday',
                    'time','lecture_type', 'isCustom_time',
                    'custom_begins', 'custom_ends')

class WeekAdmin(admin.ModelAdmin):
    list_display = ('number',)

class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['number']

admin.site.register(models.Time, TimeAdmin)
admin.site.register(models.TimetableEntry, TimetableAdmin)
admin.site.register(models.Week, WeekAdmin)
admin.site.register(models.Classroom, ClassroomAdmin)
