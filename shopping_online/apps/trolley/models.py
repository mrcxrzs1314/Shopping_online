from django.db import models

class trolley(models.Model):
    t_name = models.CharField('商品名',max_length=255)
    numbers = models.SmallIntegerField('数量')
    u_name = models.CharField('用户名',max_length=20)
    image = models.CharField('图片',max_length=500)
    price = models.SmallIntegerField('单价')
