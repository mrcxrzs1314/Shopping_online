from django.shortcuts import render
from .models import *



def index(request):
    return render(request, '../templates/base/base.html')

def login_last(request):
    return render(request, '../templates/base/main.html')


def food_air(request):
    result = air.objects.all()
    print(result)
    return render(request, '../templates/shopping/air.html',{'result': result})

def food_bai(request):
    result = bai.objects.all()
    return render(request, '../templates/shopping/bai.html',{'result': result})

def food_beef(request):
    result = beef.objects.all()
    return render(request, '../templates/shopping/beef.html',{'result': result})

def food_bread(request):
    result = bread.objects.all()
    return render(request, '../templates/shopping/bread.html',{'result': result})

def food_chicken(request):
    result = chicken.objects.all()
    return render(request, '../templates/shopping/chicken.html',{'result': result})

def food_cookie(request):
    result = cookie.objects.all()
    return render(request, '../templates/shopping/cookie.html',{'result': result})

def food_fish(request):
    result = fish.objects.all()
    return render(request, '../templates/shopping/fish.html',{'result': result})

def food_hotpot(request):
    result = hotpot.objects.all()
    return render(request, '../templates/shopping/hotpot.html',{'result': result})

def food_juice(request):
    result = juice.objects.all()
    return render(request, '../templates/shopping/juice.html',{'result': result})

def food_liang(request):
    result = liang.objects.all()
    return render(request, '../templates/shopping/liang.html',{'result': result})

def food_milk(request):
    result = milk.objects.all()
    return render(request, '../templates/shopping/milk.html',{'result': result})

def food_noodles(request):
    result = noodles.objects.all()
    return render(request, '../templates/shopping/noodles.html',{'result': result})

def food_rice(request):
    result = rice.objects.all()
    return render(request, '../templates/shopping/rice.html',{'result': result})

def food_san(request):
    result = san.objects.all()
    return render(request, '../templates/shopping/san.html',{'result': result})

def food_soda(request):
    result = soda.objects.all()
    return render(request, '../templates/shopping/soda.html',{'result': result})

def food_water(request):
    result = water.objects.all()
    return render(request, '../templates/shopping/water.html',{'result': result})



