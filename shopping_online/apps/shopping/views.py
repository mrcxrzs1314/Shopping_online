from django.shortcuts import render
from django.views import View

def shopping(request):
    return render(request, '../templates/base/main.html')
