# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0009_remove_pathgrid_density'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='longName',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
