# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20150406_0309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='note',
            new_name='notes',
        ),
    ]
