
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
   path('',include('users.urls')),
   path('',include('orders.urls')),
   path('', include('trolleys.urls')),
   path('', include('shopping.urls')),
   path('', include('verifications.urls')),

]
