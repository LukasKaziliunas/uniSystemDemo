from django.shortcuts import render, redirect
from .models import Student, Account, StudentSubjects, StudentExaminations
from django.http import HttpResponse


def home(request):
    user    = request.user
    context = {}
    if user.user_type == Account.STUDENT:
        profile = Student.objects.get(pk=user.pk)
        semester = profile.studyGroup.get_semester_display() #gauti human-readable lauko reiksme
        studentSubjects = StudentSubjects.objects.filter(student=profile, semester=profile.studyGroup.semester)
        context['user'] = user
        context['profile'] = profile
        context['semester'] = semester
        context['studentSubjects'] = studentSubjects
        return render(request, 'studentHome.html', context)
    else:
        return redirect("home")

def studentAssessments(request, id):
    user = request.user
    context = {}
    examinations_weeks = []
    range_weeks = range(1, 16)
    #ar prisijunges studentas ir ar sitas studento modulis tikrai priklauso siam prisijungusiam studentui
    if user.user_type == Account.STUDENT and StudentSubjects.objects.get(pk=id).student.pk == user.pk:
        stud_examinations = StudentExaminations.objects.filter(studentSubject=id)
        for examin in stud_examinations:
            examinations_weeks.append(examin.examination.week)

        context['stud_examinations'] = stud_examinations
        context['weeks'] = examinations_weeks
        context['range'] = range_weeks
        return render(request, 'grades.html', context)
    else:
        return redirect("home")
