from django.shortcuts import render

def trolley(request):
    return render(request, '../templates/trolley/trolley.html')
