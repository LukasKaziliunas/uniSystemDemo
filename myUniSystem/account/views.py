from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import Account_form, LoginForm, Student_form
from account.models import Account
from student.models import StudyGroup, Examination, Student, StudentSubjects, StudentExaminations
from subjects.models import FieldSubjects
from django.http import HttpResponse
import random

#studento registravimo forma
def registration_page(request):
    context = {}
    groups = StudyGroup.objects.all()
    context['groups'] = groups
    if request.POST:                                #jeigu paspausta submit
        accForm = Account_form(request.POST)
        studForm = Student_form(request.POST)
        if accForm.is_valid() and studForm.is_valid():
            account = accForm.save(commit=False)    #is abieju formu gaunu modeliu duomenis
            student = studForm.save(commit=False)
                                                    #sukuriu paskyra
            firstName = accForm.cleaned_data.get("first_name")
            lastName = accForm.cleaned_data.get("last_name")

            account.username = firstName[:3].lower() + lastName[:3].lower()
            account.user_type = Account.STUDENT
            account.save()
                                                    #sukuriu studento profili, prijungta prie paskyros
            code = codeGenerator() # reiketu patikrinti ar toks kodas neegzistuoja
            group = studForm.cleaned_data.get("studyGroup")
            phone = studForm.cleaned_data.get("phone")

            student = Student(account=account, phone=phone, code=code, studyGroup=group)
            student.save()

            createStudentCourses(student)           #db uzpildoma studento moduliais ir atsiskaitymais

            login(request, account)
            return redirect('home')
        else:                                       #jei yra klaidu tas pacias formas grazinti atgal
            context['account_form'] = accForm
            context['student_form'] = studForm
    else:                                           #jei katik atejo i registracijos puslapi, pateikia tuscias formas
        accForm = Account_form()
        studForm = Student_form()
        context['account_form'] = accForm
        context['student_form'] = studForm

    return render(request, 'register.html', context)

def login_page(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)

                return redirect("home")

    else:
        form = LoginForm()

    context['login_form'] = form
    return render(request, 'login.html', context)


def redirect_home(request):
    user = request.user
    type = user.user_type
    if type == Account.PROFESSOR:
        return redirect("professor_home")
    elif type == Account.STUDENT:
        return redirect("student_home")
    elif type == Account.UNDEFINED:
        return redirect("home")


def codeGenerator():
    letters = ["A", "B", "C", "D", "E", "F", "G"]
    randLet = random.choice(letters)
    randNum = random.randint(1000, 9999)

    return randLet + str(randNum)

#uzpildo duomenu baze kiekvieno studento moduliais ir moduliu atsiskaitymais
def createStudentCourses(student):

    subjects = student.studyGroup.subjects.all()
    field = student.studyGroup.field

    for subject in subjects:
        examinations = Examination.objects.filter(subject=subject.pk)
        semester = FieldSubjects.objects.get(subject=subject.pk, field=field.pk).semester

        studentSubject = StudentSubjects.objects.create(student=student, subject=subject, semester=semester)
        studentSubject.save()

        for examn in examinations:
            studExamin = StudentExaminations.objects.create(studentSubject=studentSubject, examination=examn)
            studExamin.save()


    return student