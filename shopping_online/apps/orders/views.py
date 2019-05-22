from django.shortcuts import render
from .models import orders

def order(request):
    result = orders.objects.all()
    return render(request, '../templates/orders/order.html',{'result': result})
