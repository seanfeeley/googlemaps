# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0005_auto_20141005_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='PathGrid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fromLocationToArea', models.BooleanField(default=True)),
                ('mode', models.CharField(max_length=200)),
                ('area', models.ForeignKey(to='directions.Area')),
                ('departure', models.ForeignKey(to='directions.Departure')),
                ('location', models.ForeignKey(to='directions.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='path',
            name='departure',
        ),
        migrations.RemoveField(
            model_name='path',
            name='location',
        ),
        migrations.RemoveField(
            model_name='path',
            name='mode',
        ),
        migrations.AddField(
            model_name='path',
            name='pathGrid',
            field=models.ForeignKey(default=0, to='directions.PathGrid'),
            preserve_default=True,
        ),
    ]
