from django.db import models

class Users(models.Model):
    username = models.CharField('用户名',max_length=20)
    password = models.CharField('密码',max_length=8)
