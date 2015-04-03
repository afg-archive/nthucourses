# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('no', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=256)),
                ('credit', models.IntegerField()),
                ('room', models.CharField(max_length=256)),
                ('capacity', models.IntegerField()),
                ('teacher', models.CharField(max_length=256)),
                ('size_limit', models.IntegerField()),
                ('note', models.TextField()),
                ('enrollment', models.IntegerField()),
                ('object', models.CharField(max_length=256)),
                ('syllabus_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('abbr', models.CharField(max_length=4)),
                ('name_zh', models.CharField(max_length=256)),
                ('name_en', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('value', models.CharField(max_length=5)),
                ('year', models.IntegerField()),
                ('section', models.IntegerField()),
                ('name', models.CharField(max_length=256)),
                ('ready', models.BooleanField(default=False)),
            ],
        ),
    ]
