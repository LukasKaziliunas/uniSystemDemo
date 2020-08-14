from django.shortcuts import render
from django.http import HttpResponse
from .models import Area, Field

def index(request):
    areas = Area.objects.all()
    return render(request, 'admission_main.html', {'areas': areas})

def load_fields(request):
    area_id = request.GET.get('area')
    fields = Field.objects.filter(area_id=area_id).order_by('name')
    return render(request, 'fields_selector.html', {'fields': fields})

def field_info(request, id):
    field = Field.objects.get(id=id)
    context = {}
    context['field'] = field
    return render(request, 'field_info.html', context)
