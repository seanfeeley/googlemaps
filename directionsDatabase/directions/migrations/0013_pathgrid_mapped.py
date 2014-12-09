# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0012_auto_20141109_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathgrid',
            name='mapped',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
