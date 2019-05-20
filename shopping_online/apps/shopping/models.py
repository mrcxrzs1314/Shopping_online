from django.db import models


class air(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "food_air"


class bai(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "bai"


class beef(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "food_beef"


class bread(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "food_bread"


class chicken(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "food_chicken"


class cookie(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "food_cookie"


class fish(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "food_fish"


class hotpot(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "food_hotpot"


class juice(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "food_juice"


class liang(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "liang"


class milk(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "food_milk"


class noodles(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "food_noodles"


class rice(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "food_rice"


class san(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "san"


class soda(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "food_soda"


class water(models.Model):
    name = models.CharField('商品名', max_length=50)
    image = models.CharField('图片', max_length=200)
    price = models.SmallIntegerField('单价')

    class Meta:
        db_table = "food_water"
