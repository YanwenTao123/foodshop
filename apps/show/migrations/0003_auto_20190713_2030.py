# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-13 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0002_auto_20190713_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='emial_type',
            new_name='email_type',
        ),
        migrations.AlterField(
            model_name='email',
            name='add_time',
            field=models.CharField(default='2019-07-13 20:30:13', max_length=30, verbose_name='加入时间'),
        ),
    ]