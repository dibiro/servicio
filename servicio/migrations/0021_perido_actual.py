# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0020_alumnos_periodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='perido',
            name='actual',
            field=models.BooleanField(default=True),
        ),
    ]
