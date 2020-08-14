from django.db import models
from admission.models import Field
from timetable import models as timetable_model


class Subject(models.Model):
    TYPES = (
        ('B', 'bachelor'),
        ('M', 'masters'),
        ('D', 'doctoral'),
    )

    TIERS = (
        ('1', 'first'),
        ('2', 'second'),
        ('3', 'third'),
        ('4', 'fourth'),

    )

    LANGUAGES = (
        ('LT', 'lithuanian'),
        ('EN', 'english'),

    )

    code = models.CharField(max_length=10, default="")
    title = models.CharField(max_length=100)
    tier = models.CharField(max_length=100, choices=TIERS)
    type = models.CharField(max_length=100, choices=TYPES)
    language = models.CharField(max_length=100, choices=LANGUAGES)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class FieldSubjects(models.Model):

    SEMESTER = (
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'),
        ('7', '7th'),
        ('8', '8th'),
    )

    semester = models.CharField(choices=SEMESTER, max_length=1)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Examination(models.Model):

    LAB_EXAM = "LB"
    MIDTERM = "MT"
    PRESENTATION = "PRE"
    PROJECT_REPORT = "PR"
    REPORT = "REP"
    FINAL_EXAM = "FE"

    TYPE = (
        (LAB_EXAM, 'laboratory examination'),
        (MIDTERM, 'Mid-term examination'),
        (PRESENTATION, 'presentation'),
        (PROJECT_REPORT, 'Project report'),
        (REPORT, 'report'),
        (FINAL_EXAM, 'final exam'),
    )




    type = models.CharField(choices=TYPE, max_length=4)
    week = models.SmallIntegerField(choices=timetable_model.WEEKS, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return "sub: %s , week: %d, type: %s" % (self.subject.title, self.week, self.get_type_display())
