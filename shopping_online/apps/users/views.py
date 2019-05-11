from django.shortcuts import render
from django.views import View


def register(request):
    return render(request, '../templates/base/register.html')
def login(request):
    return render(request, '../templates/base/login.html')
