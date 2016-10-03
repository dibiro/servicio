# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0021_perido_actual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perido',
            name='periodo',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
