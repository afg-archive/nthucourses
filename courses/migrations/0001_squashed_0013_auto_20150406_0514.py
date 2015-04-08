# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    replaces = [('courses', '0001_initial'), ('courses', '0002_auto_20150403_2321'), ('courses', '0003_auto_20150403_2325'), ('courses', '0004_auto_20150403_2332'), ('courses', '0005_auto_20150403_2339'), ('courses', '0006_auto_20150404_0018'), ('courses', '0007_auto_20150404_1708'), ('courses', '0008_auto_20150404_1715'), ('courses', '0009_auto_20150404_2017'), ('courses', '0010_auto_20150405_1905'), ('courses', '0011_auto_20150405_2357'), ('courses', '0012_auto_20150406_0309'), ('courses', '0013_auto_20150406_0514')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('abbr', models.CharField(max_length=4)),
                ('name_zh', models.CharField(max_length=256)),
                ('name_en', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('value', models.CharField(max_length=6)),
                ('year', models.IntegerField()),
                ('section', models.IntegerField()),
                ('name', models.CharField(max_length=256)),
                ('ready', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='departments',
            field=models.ManyToManyField(to='courses.Department'),
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(to='courses.Semester', default=1),
            preserve_default=False,
        ),
        migrations.RenameField(
            model_name='course',
            old_name='title',
            new_name='title_zh',
        ),
        migrations.AddField(
            model_name='course',
            name='ge_line',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisite',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='required_by',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='time',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='title_en',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='capacity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='size_limit',
            field=models.IntegerField(null=True),
        ),
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
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('departments_updated', models.DateTimeField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ('-year', '-section', '-created'), 'get_latest_by': 'created'},
        ),
        migrations.AlterField(
            model_name='course',
            name='departments',
            field=models.ManyToManyField(to='courses.Department', db_index=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='no',
            field=models.CharField(db_index=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='department',
            name='abbr',
            field=models.CharField(db_index=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='semester',
            name='value',
            field=models.CharField(db_index=True, max_length=6),
        ),
        migrations.CreateModel(
            name='SemesterEntry',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
        migrations.AlterModelOptions(
            name='semesterentry',
            options={'ordering': ('semester',)},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='syllabus_text',
            new_name='syllabus',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='note',
            new_name='notes',
        ),
    ]
