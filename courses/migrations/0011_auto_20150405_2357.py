# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20150405_1905'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='semesterentry',
            options={'ordering': ('semester',)},
        ),
    ]
