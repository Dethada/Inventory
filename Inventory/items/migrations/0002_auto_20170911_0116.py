# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 17:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 9, 10, 17, 16, 2, 813957, tzinfo=utc)),
        ),
    ]