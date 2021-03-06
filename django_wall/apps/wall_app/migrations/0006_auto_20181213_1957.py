# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-13 19:57
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0005_auto_20181213_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
