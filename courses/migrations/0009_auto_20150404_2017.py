# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20150404_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='departments',
            field=models.ManyToManyField(to='courses.Department', db_index=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='no',
            field=models.CharField(max_length=15, db_index=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='abbr',
            field=models.CharField(max_length=4, db_index=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='value',
            field=models.CharField(max_length=6, db_index=True),
        ),
    ]
