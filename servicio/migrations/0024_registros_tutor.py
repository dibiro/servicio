# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-03 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0023_remove_registros_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='registros',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicio.ProfesoresByIntituciones'),
        ),
    ]