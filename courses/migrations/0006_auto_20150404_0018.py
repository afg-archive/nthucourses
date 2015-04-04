# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20150403_2339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('no', 'semester')},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ('abbr',)},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ('-year', '-section', '-created')},
        ),
        migrations.AddField(
            model_name='course',
            name='freshmen_reserved',
            field=models.IntegerField(null=True),
        ),
    ]
