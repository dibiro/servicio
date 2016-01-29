# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0009_auto_20160122_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesores',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='profesores',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='profesores',
            name='telefono',
        ),
        migrations.AddField(
            model_name='profesores',
            name='apellidos',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profesores',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profesores',
            name='nombres',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profesores',
            name='telefono1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profesores',
            name='telefono2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profesores',
            name='direccion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
