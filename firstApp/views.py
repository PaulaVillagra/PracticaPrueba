from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def displayHola(request):
    return HttpResponse("<b>Hola</b>")
