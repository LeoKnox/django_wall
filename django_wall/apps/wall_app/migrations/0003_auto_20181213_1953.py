# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-13 19:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0002_auto_20181213_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
    ]
