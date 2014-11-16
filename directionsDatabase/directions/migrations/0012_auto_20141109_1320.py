# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0011_auto_20141109_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationinarea',
            name='note',
        ),
        migrations.RemoveField(
            model_name='path',
            name='valid',
        ),
    ]
