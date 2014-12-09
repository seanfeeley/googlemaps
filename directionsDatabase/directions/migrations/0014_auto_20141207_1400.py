# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0013_pathgrid_mapped'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pathgrid',
            name='mapped',
        ),
        migrations.AddField(
            model_name='area',
            name='mapped',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
