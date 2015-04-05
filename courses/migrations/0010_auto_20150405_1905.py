# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20150404_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='SemesterEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ready', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('no', 'semester_entry')},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ('abbr',), 'get_latest_by': 'updated'},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ('-year', '-section'), 'get_latest_by': 'updated'},
        ),
        migrations.RemoveField(
            model_name='course',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='created',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='ready',
        ),
        migrations.AddField(
            model_name='department',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 5, 11, 4, 55, 301627, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semester',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 5, 11, 5, 1, 55719, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semesterentry',
            name='semester',
            field=models.ForeignKey(to='courses.Semester'),
        ),
        migrations.AddField(
            model_name='course',
            name='semester_entry',
            field=models.ForeignKey(to='courses.SemesterEntry', default=1),
            preserve_default=False,
        ),
    ]
