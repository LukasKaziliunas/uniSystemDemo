from django.shortcuts import render
from django.http import HttpResponse

def sebjectInfo(request, id):
    return HttpResponse("modulio info %s" % id)
