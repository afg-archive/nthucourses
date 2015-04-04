from django.views.generic.base import TemplateView

from courses.forms import CourseForm
from courses.models import Semester, Department


class Result(dict):
    def __init__(self, semester, departments):
        self['semester'] = Semester.objects.get(value=semester, ready=True)
        self['departments'] = Department.objects.get(abbr=departments)
        self['courses'] = self['semester'].course_set.filter(
            departments=self['departments'])


class Course(TemplateView):
    template_name = 'courses.html'
    form_class = CourseForm

    def get(self, request):
        if request.GET:
            form = self.form_class(request.GET)
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return self.render_to_response({
                'form': self.form_class(),
            })

    def form_valid(self, form):
        print('haha')
        return self.render_to_response({
            'form': form,
            'result': Result(**form.cleaned_data)
        })

    def form_invalid(self, form):
        return self.render_to_response({
            'form': form,
        })
