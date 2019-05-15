from django.shortcuts import render
from django.views import View


def register(request):
    return render(request, '../templates/users/register.html')
def login(request):
    return render(request, '../templates/users/login.html')
def change(request):
    return render(request, '../templates/users/change.html')
