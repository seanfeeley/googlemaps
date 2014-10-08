# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0006_auto_20141005_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathgrid',
            name='density',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
