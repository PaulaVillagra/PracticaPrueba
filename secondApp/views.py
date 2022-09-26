from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def hora(request):
    dt=datetime.datetime.now()
    s="<h1>Fecha y hora actual: </h1>"+str(dt)
    return HttpResponse(s)
