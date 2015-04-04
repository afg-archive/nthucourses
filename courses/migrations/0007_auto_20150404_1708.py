# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20150404_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_list_updated', models.DateTimeField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ('-year', '-section', '-created'), 'get_latest_by': 'created'},
        ),
    ]
