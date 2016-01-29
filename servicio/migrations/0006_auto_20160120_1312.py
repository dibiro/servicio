# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 17:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0005_auto_20160120_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='escuelas',
            name='enlace',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='escuelas',
            name='estado',
            field=models.CharField(blank=True, choices=[('1', 'Activo'), ('2', 'Inactivo'), ('3', 'Descartado')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='escuelas',
            name='telefono_de_enlace',
            field=models.CharField(default=datetime.datetime(2016, 1, 20, 17, 42, 10, 979630, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reguistros',
            name='periodo',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]