# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-13 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_auto_20190713_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmsg',
            name='add_time',
            field=models.CharField(default='2019-07-13 20:30:13', max_length=50, verbose_name='添加时间'),
        ),
    ]