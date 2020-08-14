from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Professor, Account
from subjects.models import Subject
from student.models import StudentExaminations, StudentSubjects

def home(request):
    user    = request.user
    context = {}
    if user.user_type == Account.PROFESSOR:
        professor = Professor.objects.get(pk=user.pk)
        subjects = professor.subjects.all()
        context['user'] = user
        context['professor'] = professor
        context['subjects'] = subjects
        return render(request, 'professorHome.html', context)
    else:
        return redirect("home")

def subject_students(request, subject_id):
    context = {}
    user = request.user
    subject = Subject.objects.get(pk=subject_id)
    groups = subject.study_groups.all()
    context['groups'] = groups
    context['subject_id'] = subject_id
    # ar prisijunges destytojas ir ar sitas modulis jam priklauso
    if user.user_type == Account.PROFESSOR and subject.professors.filter(pk=user.pk).exists():
        return render(request, 'students_list.html', context)
    else:
        return redirect("home")

def student_grades(request, stud_id, subject_id):
    context = {}
    user = request.user
    context['id'] = subject_id
    examinations_weeks = []
    range_weeks = range(1, 16)
    student_subject = StudentSubjects.objects.get(student=stud_id, subject=subject_id)

    if user.user_type == Account.PROFESSOR:
        stud_examinations = StudentExaminations.objects.filter(studentSubject=student_subject.pk)
        for examin in stud_examinations:
            examinations_weeks.append(examin.examination.week)

        context['stud_examinations'] = stud_examinations
        context['weeks'] = examinations_weeks #kada vyks atsiskaitymai
        context['range'] = range_weeks
        context['subject'] = subject_id

        return render(request, 'student_grades.html', context)
    else:
        return redirect("home")

def saveGrades(request, subject_id):

    t = iter(request.POST.items()) #praleidzia pirma elementa POST masyve,
    next(t)                        # nes jis yra csrf_token
    try:
        for key, value in t:
            if value != '':
                student_subject = StudentExaminations.objects.get(pk=key)
                student_subject.grade = value
                student_subject.save()
        return redirect('/professor/subject/' + str(subject_id) )
    except ObjectDoesNotExist:
        return HttpResponse("error while saving grades")
