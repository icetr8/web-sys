# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-02 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20171008_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='address',
            field=models.CharField(max_length=150),
        ),
    ]
