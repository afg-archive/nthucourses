# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_auto_20150408_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='time',
        ),
        migrations.AddField(
            model_name='course',
            name='time_set',
            field=models.ManyToManyField(to='courses.Time'),
        ),
    ]
