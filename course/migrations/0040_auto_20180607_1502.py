# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-07 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0039_auto_20180326_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='anon_id',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='anon_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
