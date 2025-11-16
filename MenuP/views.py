from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Menu(request):
    return render(request, 'Menuprincipal.html')
    
