# Generated by Django 2.1.7 on 2019-05-18 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trolleys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=255, verbose_name='商品名')),
                ('numbers', models.SmallIntegerField(verbose_name='数量')),
                ('u_name', models.CharField(max_length=20, verbose_name='用户名')),
                ('image', models.CharField(max_length=500, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
        ),
    ]
