from django.urls import path, re_path

from . import views

app_name = "trolleys"

urlpatterns = [
    path('trolleys/', views.trolleys, name='trolleys'),

]