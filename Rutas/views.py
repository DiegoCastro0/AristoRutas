from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Rutas(request):
    return render(request, 'rutas.html')
