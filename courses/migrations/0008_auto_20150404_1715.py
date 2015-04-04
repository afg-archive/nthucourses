# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20150404_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meta',
            old_name='department_list_updated',
            new_name='departments_updated',
        ),
    ]
