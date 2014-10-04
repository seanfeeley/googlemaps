# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationInArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('percentageAlongX', models.FloatField(default=0)),
                ('percentageAlongY', models.FloatField(default=0)),
                ('area', models.ForeignKey(to='directions.Area')),
                ('location', models.ForeignKey(to='directions.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arrival', models.DateTimeField(verbose_name=b'Arrival time')),
                ('actualDeparture', models.DateTimeField(verbose_name=b'Actual departure time')),
                ('mode', models.CharField(max_length=200)),
                ('seconds', models.IntegerField(default=0)),
                ('departure', models.ForeignKey(to='directions.Departure')),
                ('location', models.ForeignKey(to='directions.Location')),
                ('locationInArea', models.ForeignKey(to='directions.LocationInArea')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SingleLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('location', models.ForeignKey(to='directions.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='directions',
            name='area',
        ),
        migrations.RemoveField(
            model_name='directions',
            name='departure',
        ),
        migrations.RemoveField(
            model_name='directions',
            name='location',
        ),
        migrations.DeleteModel(
            name='Directions',
        ),
        migrations.RemoveField(
            model_name='location',
            name='name',
        ),
    ]
