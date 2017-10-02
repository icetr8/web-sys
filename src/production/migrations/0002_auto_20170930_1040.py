# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-30 02:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvest',
            name='employee_attended',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]