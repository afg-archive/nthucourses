# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_create_time_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='time',
            options={'ordering': ('index',)},
        ),
    ]
