from django.shortcuts import render
from django.views import View

def index(request):
    return render(request, '../templates/base/base.html')
def shopping(request):
    return render(request, '../templates/shopping/shopping.html')

