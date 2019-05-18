import re
from django import forms
from django.contrib.auth import login
from django.db.models import Q
from .constants import USER_SESSION_EXPIRES
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
        """
        验证两次密码是否相同
        """
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
    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)


