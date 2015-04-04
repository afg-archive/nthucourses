# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20150403_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='departments',
            field=models.ManyToManyField(to='courses.Department'),
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(to='courses.Semester', default=1),
            preserve_default=False,
        ),
    ]
