# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150403_2325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='title',
            new_name='title_zh',
        ),
        migrations.AddField(
            model_name='course',
            name='ge_line',
            field=models.CharField(max_length=256, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisite',
            field=models.CharField(max_length=256, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='required_by',
            field=models.CharField(max_length=256, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='time',
            field=models.CharField(max_length=256, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='title_en',
            field=models.CharField(max_length=256, default=''),
            preserve_default=False,
        ),
    ]
