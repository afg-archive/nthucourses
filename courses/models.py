from django.db import models
from django.core.urlresolvers import reverse


TYPICAL_SIZE = 256


class Semester(models.Model):
    value = models.CharField(max_length=6, db_index=True)
    year = models.IntegerField()
    section = models.IntegerField()
    name = models.CharField(max_length=TYPICAL_SIZE)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-year', '-section')
        get_latest_by = 'updated'

    def __str__(self):
        return self.value


class SemesterEntry(models.Model):
    semester = models.ForeignKey(Semester)
    created = models.DateTimeField(auto_now_add=True)
    ready = models.BooleanField(default=False)

    class Meta:
        ordering = ('semester',)

    def __str__(self):
        return '{}, {}'.format(self.semester.value, self.created)


class Time(models.Model):
    index = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=2, db_index=True)

    class Meta:
        ordering = ('index',)

    def __str__(self):
        return self.name


class Department(models.Model):
    abbr = models.CharField(max_length=4, db_index=True)
    name_zh = models.CharField(max_length=TYPICAL_SIZE)
    name_en = models.CharField(max_length=TYPICAL_SIZE)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('abbr',)
        get_latest_by = 'updated'

    def __str__(self):
        return self.abbr


class Course(models.Model):
    semester_entry = models.ForeignKey(SemesterEntry, db_index=True)
    departments = models.ManyToManyField(Department, db_index=True)
    no = models.CharField(max_length=15, db_index=True)
    title_zh = models.CharField(max_length=TYPICAL_SIZE)
    title_en = models.CharField(max_length=TYPICAL_SIZE)
    ge_line = models.CharField(max_length=TYPICAL_SIZE)
    credit = models.IntegerField()
    time_set = models.ManyToManyField(Time)
    room = models.CharField(max_length=TYPICAL_SIZE)
    capacity = models.IntegerField(null=True)
    teacher = models.CharField(max_length=TYPICAL_SIZE)
    size_limit = models.IntegerField(null=True)
    freshmen_reserved = models.IntegerField(null=True)
    notes = models.TextField()
    enrollment = models.IntegerField()
    object = models.CharField(max_length=TYPICAL_SIZE)
    prerequisite = models.CharField(max_length=TYPICAL_SIZE)  # TODO
    required_by = models.CharField(max_length=TYPICAL_SIZE)  # TODO
    syllabus = models.TextField()
    syllabus_attachment = None  # TODO

    class Meta:
        ordering = ('no', 'semester_entry')

    def __str__(self):
        return self.no

    def get_absolute_url(self):
        return reverse(
            'course',
            kwargs={
                'no': self.no,
            }
        )
        return reverse('course', kwargs={'pk': self.pk})

    def todict(self):
        fields = (
            'pk',
            'no',
            'title_zh',
            'ge_line',
            'credit',
            'time',
            'room',
            'teacher',
            'size_limit',
            'freshmen_reserved',
            'notes',
            'enrollment',
            'object',
            'prerequisite',
            'required_by',
            'time_indexer',
            'time_indexes'
        )
        result = {field: getattr(self, field) for field in fields}
        result['href'] = self.get_absolute_url()
        return result

    @property
    def time(self):
        return ''.join(map(str, self.time_set.all()))

    @property
    def time_indexer(self):
        return ''.join(
            format(time.index, '02d') for time in self.time_set.all())

    @property
    def time_indexes(self):
        return [time.index for time in self.time_set.all()]
