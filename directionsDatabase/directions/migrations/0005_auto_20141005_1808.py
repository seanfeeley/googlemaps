# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0004_auto_20141005_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='path',
            name='actualDeparture',
        ),
        migrations.RemoveField(
            model_name='path',
            name='arrival',
        ),
        migrations.AddField(
            model_name='path',
            name='delay',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
