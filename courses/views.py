from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from courses.forms import CourseForm
from courses.models import SemesterEntry, Department, Course


class Result(dict):
    def __init__(self, semester, departments, teacher, title, timeoperation):
        entry = SemesterEntry.objects.get(
            semester__value=semester,
            ready=True)
        semester = entry.semester
        courses = entry.course_set.all()
        if departments:
            departments = Department.objects.filter(abbr__in=departments)
            courses = courses = courses.filter(departments__in=departments)
        if teacher:
            courses = courses.filter(teacher=teacher)
        if title:
            courses = courses.filter(title_zh=title)
        self['semester'] = semester.name
        self['semester_code'] = semester.value
        self['courses'] = [course.todict() for course in courses[:200]]
        self.updated = entry.created  # not json serializable


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


class CourseView(DetailView):
    template_name = 'course.html'
    model = Course

    def get_context_data(self, *, object):
        context = super().get_context_data(object=object)
        context['past_years'] = Course.objects.filter(
            semester_entry__ready=True,
            title_zh=object.title_zh,
        ).order_by(
            '-semester_entry__semester__year',
            '-enrollment',
        )
        return context
