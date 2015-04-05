# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20150405_2357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='syllabus_text',
            new_name='syllabus',
        ),
    ]
