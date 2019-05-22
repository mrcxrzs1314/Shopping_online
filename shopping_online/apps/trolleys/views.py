from django.shortcuts import render
from .models import trolley

def trolleys(request):
    result = trolley.objects.all()
    return render(request, '../templates/trolley/trolley.html',{'result': result})
