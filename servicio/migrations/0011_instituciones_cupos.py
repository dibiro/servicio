# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 18:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0010_auto_20160123_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='instituciones',
            name='cupos',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]