# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import itertools

from django.db import models, migrations


def get_times():
    return [''.join(timespec) for timespec in itertools.product(
        'MTWRFS', '1234n56789abc')]


def create_time_data(apps, schema_editor):
    Time = apps.get_model('courses', 'Time')
    for n, time in enumerate(get_times()):
        Time.objects.create(index=n, name=time)


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_time'),
    ]

    operations = [
        migrations.RunPython(create_time_data),
    ]
