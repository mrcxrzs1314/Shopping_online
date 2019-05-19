import re
from django import forms
from django.contrib.auth import login
from django.db.models import Q
from users.models import Users

class RegisterForm(forms.Form):

    username = forms.CharField(label='用户名', max_length=20, min_length=3,
                               error_messages={"min_length": "用户名长度要大于3", "max_length": "用户名长度要小于20",
                                               "required": "用户名不能为空"}
                               )
    password = forms.CharField(label='密码', max_length=20, min_length=3,
                               error_messages={"min_length": "密码长度要大于3", "max_length": "密码长度要小于20",
                                               "required": "密码不能为空"}
                               )
    password_repeat = forms.CharField(label='确认密码', max_length=20, min_length=3,
                                      error_messages={"min_length": "密码长度要大于3", "max_length": "密码长度要小于20",
                                                      "required": "密码不能为空"}
                                      )


    def clean(self):

        cleaned_data = super().clean()
        passwd = cleaned_data.get('password')
        passwd_repeat = cleaned_data.get('password_repeat')

        if passwd != passwd_repeat:

            raise forms.ValidationError("两次密码不一致")


class LoginForm(forms.Form):

    user_account = forms.CharField()
    password = forms.CharField(label='密码', max_length=20, min_length=3,
                               error_messages={"min_length": "密码长度要大于3", "max_length": "密码长度要小于20",
                                               "required": "密码不能为空"})
    remember_me = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        """
        """
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean_user_account(self):
        """
        """
        user_info = self.cleaned_data.get('user_account')
        if not user_info:
            raise forms.ValidationError("用户账号不能为空")
        return user_info

    def clean(self):
        """
        """
        cleaned_data = super().clean()
        # 获取用户账号
        user_info = cleaned_data.get('user_account')
        # 获取密码
        passwd = cleaned_data.get('password')

        # 在form表单中实现登录逻辑
        user_queryset = Users.objects.filter(Q(username=user_info))
        if user_queryset:
            user = user_queryset.first()
            if user.check_password(passwd):
                login(self.request, user)
            else:
                raise forms.ValidationError("密码不正确，请重新输入")

        else:
            raise forms.ValidationError("用户账号不存在，请重新输入")


