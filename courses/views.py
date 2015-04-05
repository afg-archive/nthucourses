from django.views.generic.base import TemplateView

from courses.forms import CourseForm
from courses.models import Semester, SemesterEntry, Department


class Result(dict):
    def __init__(self, semester, departments):
        entry = SemesterEntry.objects.get(
            semester__value=semester,
            ready=True)
        semester = entry.semester
        departments = Department.objects.get(abbr=departments)
        courses = entry.course_set.filter(departments=departments)
        self['semester'] = semester.name
        self['departments'] = departments.name_zh
        self['courses'] = [course.todict() for course in courses]


class Curriculum(TemplateView):
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
