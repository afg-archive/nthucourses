from django.views.generic.base import TemplateView

from courses.models import Semester, Department


class Status(TemplateView):
    template_name = 'status.html'

    def get_context_data(self):
        return {
            'Department': Department,
            'Semester': Semester,
        }


class About(TemplateView):
    template_name = 'about.html'
