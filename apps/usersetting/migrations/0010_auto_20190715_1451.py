# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-15 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersetting', '0009_auto_20190713_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavemsg',
            name='add_time',
            field=models.CharField(default='2019-07-15', max_length=30, verbose_name='加入时间'),
        ),
    ]