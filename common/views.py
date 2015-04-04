from django.views.generic.base import TemplateView

from courses.models import Semester, Department, Course, Meta


class Index(TemplateView):
    template_name = 'index.html'


class Status(TemplateView):
    template_name = 'status.html'

    def get_context_data(self):
        return {
            'department_count': Department.objects.count(),
            'semester_count': Semester.objects.count(),
            'semesters': Semester.objects.all(),
            'meta': Meta.get(),
        }
