# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0015_auto_20160124_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registros',
            name='fecha_de_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='registros',
            name='fecha_de_fin',
            field=models.DateField(blank=True, null=True),
        ),
    ]
