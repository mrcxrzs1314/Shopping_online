
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
   path('',include('users.urls')),
   path('',include('orders.urls')),
   path('',include('trolley.urls')),
   path('', include('shopping.urls')),
   path('', include('verifications.urls')),

]
