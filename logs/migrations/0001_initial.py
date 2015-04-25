# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('message', models.CharField(max_length=256)),
                ('exc_name', models.CharField(max_length=256, default='')),
                ('traceback', models.TextField(default='')),
                ('success', models.NullBooleanField()),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('ended', models.DateTimeField(null=True)),
            ],
        ),
    ]
