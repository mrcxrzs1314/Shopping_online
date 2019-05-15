from django.db import models


class shopping(models.Model):
    food_name = models.CharField('商品名', max_length=255)
    image = models.CharField('图片',max_length=500)
    price = models.SmallIntegerField('单价')
    classify = models.CharField('分类', max_length=100)

