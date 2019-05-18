from django.shortcuts import render
from django.views import View
from django.contrib.auth import login
from .forms import RegisterForm, LoginForm
from .models import Users
from utils.json_fun import to_json_data
from utils.res_code import Code, error_map


class RegisterView(View):

    def get(self, request):
        return render(request, '../templates/users/register.html')

    def post(self, request):
        username = request.POST.get("registname")
        password = request.POST.get("registpassword")
        print(username, password)
        u = Users.objects.filter(username=username)
        if not u:
            user = Users.objects.create_user(username=username, password=password)
            login(request, user)
            return render(request, '../templates/base/main.html')
        else:
            return render(request, 'users/register.html', {'errmsg': '用户名已经被使用'})


class LoginView(View):

    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST.get("loginname")
        password = request.POST.get("loginpassword")
        print(username, password)
        user = Users.objects.filter(username=username)
        p = Users.objects.filter(username=username, password=password)
        if not user:
            if p:
                login(request, user)
                return render(request, '../templates/base/main.html')
            else:
                return render(request, 'users/login.html', {'errmsg': '密码错误'})
        else:
            return render(request, 'users/login.html', {'errmsg': '用户名已经被使用'})
