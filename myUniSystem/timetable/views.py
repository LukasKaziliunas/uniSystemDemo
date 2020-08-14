from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models import Account
from .forms import TimetableEntry_form, WeeksSelection_form
from .models import Week,  Time
from student.models import Student, StudentSubjects
from professor.models import Professor

def index(request):
    return HttpResponse("timetable index")


def week_timetable(request):
    context = {}
    week = request.GET.get('week')
    #week = 4
    user = request.user
    weekObj = Week.objects.get(pk=week)

    # m = [time][weekday][lectures] , ta pacia diena tuo paciu metu paskaitos gali duplikuotis
    #       /pir/ant/tr/ket/pen
    timetableMatrix = [[
            [], [], [], [], []
        ],
        [
            [], [], [], [], []
        ],
        [
            [], [], [], [], []
        ],
        [
            [], [], [], [], []
        ],
        [
            [], [], [], [], []
        ]
    ]

    if user.user_type == Account.STUDENT:
        student = Student.objects.get(pk=user.pk)
        semester = student.studyGroup.semester
        stud_subjects = StudentSubjects.objects.filter(semester=semester, student=student.pk)
        #context['stud_sub'] = stud_subjects

        for stud_subject in stud_subjects:                                                # eina per visus esamo semestro studento modulius
            temp_list = weekObj.timetablesEntries.filter(subject=stud_subject.subject.pk) # gauna studento modulio paskaitas
            timetableMatrix = putToMatrix(timetableMatrix,temp_list)                      # paskaitas sudeda i matrica

    elif user.user_type == Account.PROFESSOR:
        professor = Professor.objects.get(pk=user.pk)
        subjects = professor.subjects.all()
        for subject in subjects:                                                # eina per visus esamo semestro studento modulius
            temp_list = weekObj.timetablesEntries.filter(subject=subject.pk) # gauna studento modulio paskaitas
            timetableMatrix = putToMatrix(timetableMatrix,temp_list)

    else:
        return HttpResponse("incorect user")

    context['times'] = Time.objects.all()
    context['timetable'] = timetableMatrix

    return render(request, 'timetable.html', context)

def make_timetableEntry(request):
    context = {}
    if request.POST:  # jeigu paspausta submit
        timetableEntry_form = TimetableEntry_form(request.POST)
        weeksSelection_form = WeeksSelection_form(request.POST)
        if timetableEntry_form.is_valid() and weeksSelection_form.is_valid():

            timetable = timetableEntry_form.save(commit=True)  # is abieju formu gaunu duomenis
            weeksList = weeksSelection_form.cleaned_data.get("weeks")
            # weeksList = request.POST.getlist('weeks') vaikia taip pat

            #i saveiciu manyToMany lentele idedu sukurta timetable objekta (kiekvienai pazymetai savaitei tas pats timetable)
            for week in weeksList:
                weekObj = Week.objects.get(pk=week)
                weekObj.timetablesEntries.add(timetable)

            return redirect('name_new_timetable')
        else:  # jei yra klaidu tas pacias formas grazinti atgal
            context['timetableEntry_form'] = timetableEntry_form
            context['weeksSelection_form'] = weeksSelection_form
    else:  # jei katik atejo i registracijos puslapi, pateikia tuscias formas
        timetableEntry_form = TimetableEntry_form()
        weeksSelection_form = WeeksSelection_form()
        context['timetableEntry_form'] = timetableEntry_form
        context['weeksSelection_form'] = weeksSelection_form

    return render(request, 'newTimetable.html', context)


def is_even(number):
    return number % 2 == 0

def putToMatrix(matrix, entries):
    for t_entry in entries:
        weekday = t_entry.weekday #gaunu savaites dienos ir laiko indexus
        time = t_entry.time.pk
        matrix[time-1][weekday-1].append(t_entry)
    return matrix
