# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-11 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersetting', '0007_auto_20190711_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='男', max_length=10, verbose_name='性别'),
        ),
    ]
