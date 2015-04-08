# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_squashed_0013_auto_20150406_0514'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Meta',
        ),
    ]
