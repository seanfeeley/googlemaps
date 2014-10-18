# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0007_pathgrid_density'),
    ]

    operations = [
        migrations.AddField(
            model_name='path',
            name='valid',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
