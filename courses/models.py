from django.db import models


TYPICAL_SIZE = 256


class Semester(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=5)
    year = models.IntegerField()
    section = models.IntegerField()
    name = models.CharField(max_length=TYPICAL_SIZE)
    ready = models.BooleanField(default=False)


class Department(models.Model):
    abbr = models.CharField(max_length=4)
    name_zh = models.CharField(max_length=TYPICAL_SIZE)
    name_en = models.CharField(max_length=TYPICAL_SIZE)


class Course(models.Model):
    no = models.CharField(max_length=15)
    title = models.CharField(max_length=TYPICAL_SIZE)
    credit = models.IntegerField()
    time = None  # TODO
    room = models.CharField(max_length=TYPICAL_SIZE)
    capacity = models.IntegerField()
    teacher = models.CharField(max_length=TYPICAL_SIZE)
    size_limit = models.IntegerField()
    note = models.TextField()
    enrollment = models.IntegerField()
    object = models.CharField(max_length=TYPICAL_SIZE)
    required_by = None  # TODO
    prerequisite = None  # TODO
    syllabus_text = models.TextField()
    syllabus_attachment = None  # TODO
