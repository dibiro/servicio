# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0014_auto_20160124_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registros',
            name='fecha_de_creacion',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='registros',
            name='fecha_de_inicio',
            field=models.DateField(blank=True, null=True),
        ),
    ]
