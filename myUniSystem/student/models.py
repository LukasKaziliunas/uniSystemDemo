from django.db import models
from admission.models import Field
from account.models import Account
from subjects.models import Subject
from professor.models import Professor
from subjects.models import Examination, FieldSubjects


class StudyGroup(models.Model):
    code = models.CharField(max_length=10)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, through='GroupSubjects', related_name='study_groups')
    semester = models.CharField(choices=FieldSubjects.SEMESTER, max_length=1)
    def __str__(self):
        return self.code


class Student(models.Model):
    studyGroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    avarageScore = models.IntegerField(default=0)
    phone = models.CharField(max_length=15)
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    subjects = models.ManyToManyField(Subject, through='StudentSubjects', related_name='students')

    def __str__(self):
        return self.code + " " + self.account.first_name + " " + self.account.last_name


class StudentSubjects(models.Model):


    student = models.ForeignKey(Student, related_name='student_subjects', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='student_subjects', on_delete=models.CASCADE)
    semester = models.CharField(choices=FieldSubjects.SEMESTER, max_length=1)
    final_grade = models.SmallIntegerField(default=0)

    def __str__(self):
        return "stud: %s , subject: %s" % (self.student.code, self.subject.title)


class StudentExaminations(models.Model):
    grade = models.IntegerField(default=0)
    studentSubject = models.ForeignKey(StudentSubjects, on_delete=models.CASCADE)
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['studentSubject', 'examination'], name='unique_examinations')
        ]

    def __str__(self):
        return "%d" % self.examination.id


class GroupSubjects(models.Model):

    semester    = models.CharField(choices=FieldSubjects.SEMESTER, max_length=1)
    professor   = models.ForeignKey(Professor, on_delete=models.CASCADE)
    study_group = models.ForeignKey(StudyGroup, related_name='group_subjects', on_delete=models.CASCADE)
    subject     = models.ForeignKey(Subject, related_name='group_subjects', on_delete=models.CASCADE)
