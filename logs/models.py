from django.db import models
from django.utils import timezone

import traceback


class Log(models.Model):
    message = models.CharField(max_length=256)
    exc_name = models.CharField(max_length=256, default='')
    traceback = models.TextField(default='')
    success = models.NullBooleanField()
    started = models.DateTimeField(auto_now_add=True)
    ended = models.DateTimeField(null=True)

    def __str__(self):
        return '{self.message}: {self.status}'.format(self=self)

    @property
    def status(self):
        if self.success is None:
            return 'running'
        elif self.success:
            return 'success'
        else:
            return 'failure'


class Logger:
    def __init__(self, message):
        self.log = Log.objects.create(message=message)

    def __enter__(self):
        return self.log

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.log.ended = timezone.now()
        if exc_type is None:
            self.log.success = True
        else:
            self.log.success = False
            self.log.exc_name = exc_type.__name__
            self.log.traceback = ''.join(
                traceback.format_exception(exc_type, exc_val, exc_tb)
            )
        self.log.save()
