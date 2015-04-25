# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_delete_meta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('index', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=2, db_index=True)),
            ],
        ),
    ]
