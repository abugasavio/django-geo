# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('wmoid', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('geom', djgeojson.fields.PointField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
