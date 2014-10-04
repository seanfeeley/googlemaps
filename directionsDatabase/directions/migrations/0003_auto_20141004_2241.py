# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0002_auto_20141004_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='singlelocation',
            name='location',
        ),
        migrations.DeleteModel(
            name='SingleLocation',
        ),
        migrations.RemoveField(
            model_name='locationinarea',
            name='location',
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='locationinarea',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='locationinarea',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
