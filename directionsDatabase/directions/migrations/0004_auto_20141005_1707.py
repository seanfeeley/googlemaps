# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0003_auto_20141004_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationinarea',
            name='percentageAlongX',
        ),
        migrations.RemoveField(
            model_name='locationinarea',
            name='percentageAlongY',
        ),
    ]
