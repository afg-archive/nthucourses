from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView, RedirectView

from courses.models import Semester, Department


class Index(RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('courses')


class Status(TemplateView):
    template_name = 'status.html'

    def get_context_data(self):
        return {
            'Department': Department,
            'Semester': Semester,
        }


class About(TemplateView):
    template_name = 'about.html'
