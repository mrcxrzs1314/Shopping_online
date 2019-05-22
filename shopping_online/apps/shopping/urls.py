from django.urls import path, re_path

from . import views

app_name = "shopping"

urlpatterns = [
    path('', views.index, name='index'),
    path('pay/', views.pay, name='pay'),
    path('shopping_online/', views.login_last, name='shopping_online'),
    path('air/', views.food_air, name='air'),
    path('bai/', views.food_bai, name='bai'),
    path('beef/', views.food_beef, name='beef'),
    path('bread/', views.food_bread, name='bread'),
    path('chicken/', views.food_chicken, name='chicken'),
    path('cookie/', views.food_cookie, name='cookie'),
    path('fish/', views.food_fish, name='fish'),
    path('hotpot/', views.food_hotpot, name='hotpot'),
    path('juice/', views.food_juice, name='juice'),
    path('liang/', views.food_liang, name='liang'),
    path('milk/', views.food_milk, name='milk'),
    path('noodles/', views.food_noodles, name='noodles'),
    path('rice/', views.food_rice, name='rice'),
    path('san/', views.food_san, name='san'),
    path('soda/', views.food_soda, name='soda'),
    path('water/', views.food_water, name='water'),

]
