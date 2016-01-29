# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 01:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escuelas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('telefono', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'escuelas',
            },
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=50, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('sexo', models.CharField(blank=True, choices=[('1', 'Masculino'), ('2', 'Femenino')], max_length=2, null=True)),
                ('tipo', models.CharField(blank=True, choices=[('1', 'Profesor'), ('2', 'Alunno')], max_length=2, null=True)),
                ('estado', models.CharField(blank=True, choices=[('1', 'No Aplica'), ('2', 'Reguistrado'), ('3', 'Asignado'), ('4', 'Culminado')], max_length=2, null=True)),
                ('fecha_de_nacimiento', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'personas',
            },
        ),
        migrations.CreateModel(
            name='Reguistros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True)),
                ('escuela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.Escuelas')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudiante', to='servicio.Personas', unique=True)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.Personas')),
            ],
            options={
                'db_table': 'reguistros',
            },
        ),
    ]
