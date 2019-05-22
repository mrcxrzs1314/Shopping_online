from django.db import models

class orders(models.Model):
    o_name = models.CharField('商品名', max_length=255)
    numbers = models.SmallIntegerField('数量')
    u_name = models.CharField('用户名', max_length=20)
    image = models.CharField('图片',max_length=500)
    s_price = models.SmallIntegerField('总价')
    status = models.CharField('状态',max_length=6)
    address = models.CharField('地址',max_length=255)
    phone = models.CharField('手机号',max_length=11)
