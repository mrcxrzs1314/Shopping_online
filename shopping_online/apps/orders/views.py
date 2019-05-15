from django.shortcuts import render

def order(request):
    return render(request, '../templates/orders/order.html')
