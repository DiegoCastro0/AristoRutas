from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Rutas(request):
    return render(request, 'rutas.html')

def urbanas(request):
    return render(request, 'urbanas.html')

def interurbanas(request):
    return render(request, 'interurbanas.html')

def interdepartamentales(request):
    return render(request, 'interdepartamentales.html')