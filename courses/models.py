from django.db import models
from django.utils import timezone


TYPICAL_SIZE = 256


class Meta(models.Model):
    departments_updated = models.DateTimeField()

    @classmethod
    def get(cls):
        if cls.objects.count():
            return cls.objects.get()
        else:
            return cls.objects.create(
                department_list_updated=timezone.now(),
            )


class Semester(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    value = models.CharField(max_length=6)
    year = models.IntegerField()
    section = models.IntegerField()
    name = models.CharField(max_length=TYPICAL_SIZE)
    ready = models.BooleanField(default=False)

    class Meta:
        ordering = ('-year', '-section', '-created')
        get_latest_by = 'created'

    def __str__(self):
        return self.value


class Department(models.Model):
    abbr = models.CharField(max_length=4)
    name_zh = models.CharField(max_length=TYPICAL_SIZE)
    name_en = models.CharField(max_length=TYPICAL_SIZE)

    class Meta:
        ordering = ('abbr',)

    def __str__(self):
        return self.abbr


class Course(models.Model):
    semester = models.ForeignKey(Semester)
    departments = models.ManyToManyField(Department)
    no = models.CharField(max_length=15)
    title_zh = models.CharField(max_length=TYPICAL_SIZE)
    title_en = models.CharField(max_length=TYPICAL_SIZE)
    ge_line = models.CharField(max_length=TYPICAL_SIZE)
    credit = models.IntegerField()
    time = models.CharField(max_length=TYPICAL_SIZE)  # TODO
    room = models.CharField(max_length=TYPICAL_SIZE)
    capacity = models.IntegerField(null=True)
    teacher = models.CharField(max_length=TYPICAL_SIZE)
    size_limit = models.IntegerField(null=True)
    freshmen_reserved = models.IntegerField(null=True)
    note = models.TextField()
    enrollment = models.IntegerField()
    object = models.CharField(max_length=TYPICAL_SIZE)
    prerequisite = models.CharField(max_length=TYPICAL_SIZE)  # TODO
    required_by = models.CharField(max_length=TYPICAL_SIZE)  # TODO
    syllabus_text = models.TextField()
    syllabus_attachment = None  # TODO

    class Meta:
        ordering = ('no', 'semester')

    def __str__(self):
        return self.no
