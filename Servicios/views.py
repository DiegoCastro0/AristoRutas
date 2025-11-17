from django.shortcuts import render

# Create your views here.

def upgrade_plan(request):
    return render(request, 'upgrade_plan.html')