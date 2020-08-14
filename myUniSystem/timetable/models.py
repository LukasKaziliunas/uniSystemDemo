from django.db import models
#from subjects.models import Subject
from datetime import datetime

WEEKS = (
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13),
        (14, 14), (15, 15), (16, 16)
    )

class Time(models.Model):
    begins = models.TimeField()
    ends = models.TimeField()

    def __str__(self):
        return self.begins.strftime("%H:%M") + " - " + self.ends.strftime("%H:%M")

class Classroom(models.Model):
    number = models.CharField(max_length=10)

    def __str__(self):
         return self.number


class TimetableEntry(models.Model):

    #savaite
    ODD         = '1'
    EVEN        = '2'
    BOTH        = '3'

    #saveites dienos
    MONDAY      = 1
    TUESDAY     = 2
    WEDNESDAY   = 3
    THIRSDAY    = 4
    FRIDAY      = 5
    SATURDAY    = 6
    SUNDAY      = 7

    #paskaitos tipas
    LAB       = '1'
    THEORY    = '2'
    PRACTICAL = '3'


    LECTURE_TYPE = (
        (LAB, 'laboratory'),
        (THEORY, 'theory class'),
        (PRACTICAL, 'practical class'),
    )
    """
    WEEK = (
        (ODD, 'odd'),
        (EVEN, 'even'),
        (BOTH, 'both'),
    )"""

    WEEKDAY = (
        ( MONDAY, 'monday'),
        ( TUESDAY, 'tuesday'),
        ( WEDNESDAY, 'wednesday'),
        ( THIRSDAY, 'thursday'),
        ( FRIDAY, 'friday'),
        ( SATURDAY, 'saturday'),
        ( SUNDAY, 'sunday'),
    )

    subject         = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE)
    #week            = models.CharField(choices=WEEK, max_length=1)
    weekday         = models.SmallIntegerField(choices=WEEKDAY)
    time            = models.ForeignKey(Time, on_delete=models.CASCADE, default=1)
    lecture_type    = models.CharField(choices=LECTURE_TYPE, max_length=1)
    isCustom_time   = models.BooleanField(default=False)
    custom_begins   = models.TimeField(null=True, blank=True)
    custom_ends     = models.TimeField(null=True, blank=True)
    classrooms = models.ManyToManyField(Classroom, blank=True, related_name="subjects")

    def __str__(self):
        return "sub: %s , weekday: %s, time: %s, type: %s" % (self.subject, self.get_weekday_display(), self.time, self.get_lecture_type_display())


class Week(models.Model):

    number = models.SmallIntegerField(null=False)
    timetablesEntries = models.ManyToManyField(TimetableEntry, related_name="weeks", blank=True)
