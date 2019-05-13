from django.shortcuts import render
from django.views import View


def register(request):
    return render(request, '../templates/base/../../templates/users/register.html')
def login(request):
    return render(request, '../templates/base/../../templates/users/login.html')
