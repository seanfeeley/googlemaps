# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0010_area_longname'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationinarea',
            name='note',
            field=models.CharField(default=b'not set', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='locationinarea',
            name='valid',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
