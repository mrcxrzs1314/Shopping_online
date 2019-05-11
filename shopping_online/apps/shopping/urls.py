from django.urls import path, re_path

from . import views

app_name = "shopping"

urlpatterns = [
    path('shopping/', views.shopping, name='shopping'),

]
