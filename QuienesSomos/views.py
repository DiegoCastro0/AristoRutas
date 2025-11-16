from django.shortcuts import render

# Create your views here.
def Quienes(request):
	return render(request, 'QuienesSomos.html')
