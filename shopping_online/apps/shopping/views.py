from django.shortcuts import render
from django.views import View
from users.models import Users


def index(request):
    return render(request, '../templates/base/base.html')


def login_last(request):

    return render(request, '../templates/base/main.html')


def shopping(request):
    return render(request, '../templates/shopping/shopping.html')

