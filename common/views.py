import platform

import django
from django.views.generic.base import TemplateView

from courses.models import Semester, Department
from logs.models import Log


class Status(TemplateView):
    template_name = 'status.html'

    def get_context_data(self):
        return {
            'Department': Department,
            'Semester': Semester,
            'Log': Log,
        }


class About(TemplateView):
    template_name = 'about.html'

    def get_context_data(self):
        return {
            'python_version': platform.python_version(),
            'django_version': django.get_version(),
        }
