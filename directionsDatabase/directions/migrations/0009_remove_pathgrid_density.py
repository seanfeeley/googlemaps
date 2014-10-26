# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0008_path_valid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pathgrid',
            name='density',
        ),
    ]
