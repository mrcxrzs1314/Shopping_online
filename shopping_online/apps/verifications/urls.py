from django.urls import path, re_path
from . import views

app_name = "verifications"


urlpatterns = [
    re_path('username/(?P<username>\w{5,20})/', views.CheckUsernameView.as_view(), name='check_username'),

]