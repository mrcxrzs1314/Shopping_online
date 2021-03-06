# Generated by Django 2.1.7 on 2019-05-22 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='air',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'food_air',
            },
        ),
        migrations.CreateModel(
            name='bai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'bai',
            },
        ),
        migrations.CreateModel(
            name='beef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'food_beef',
            },
        ),
        migrations.CreateModel(
            name='bread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'food_bread',
            },
        ),
        migrations.CreateModel(
            name='chicken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'food_chicken',
            },
        ),
        migrations.CreateModel(
            name='cookie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'food_cookie',
            },
        ),
        migrations.CreateModel(
            name='fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'food_fish',
            },
        ),
        migrations.CreateModel(
            name='hotpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'food_hotpot',
            },
        ),
        migrations.CreateModel(
            name='juice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'food_juice',
            },
        ),
        migrations.CreateModel(
            name='liang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'liang',
            },
        ),
        migrations.CreateModel(
            name='milk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'food_milk',
            },
        ),
        migrations.CreateModel(
            name='noodles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'food_noodles',
            },
        ),
        migrations.CreateModel(
            name='rice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'food_rice',
            },
        ),
        migrations.CreateModel(
            name='san',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'san',
            },
        ),
        migrations.CreateModel(
            name='soda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'food_soda',
            },
        ),
        migrations.CreateModel(
            name='water',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='商品名')),
                ('image', models.CharField(max_length=200, verbose_name='图片')),
                ('price', models.SmallIntegerField(verbose_name='单价')),
            ],
            options={
                'db_table': 'food_water',
            },
        ),
    ]
