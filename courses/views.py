from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from courses.forms import CourseForm, TimeForm
from courses.models import SemesterEntry, Department, Course, Time


def get_time_table():
    return zip(*zip(* [iter(Time.objects.all())] * 13))


class Result(dict):
    def __init__(self, semester, departments, teacher, title, timeoperation, time):
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
        if timeoperation == 'exclude':
            db_time = Time.objects.filter(pk__in=time)
        else:
            db_time = Time.objects.exclude(pk__in=time)
        courses = courses.exclude(time_set__in=db_time)
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
            time_form = TimeForm(request.GET)
            if form.is_valid() and time_form.is_valid():
                return self.form_valid(form, time_form)
            else:
                return self.form_invalid(form, time_form)
        else:
            return self.render_to_response({
                'form': self.form_class(),
                'time_form': TimeForm(),
            })

    def form_valid(self, form, time_form):
        return self.render_to_response({
            'form': form,
            'time_form': time_form,
            'result': Result(time=time_form.cleaned_data['time'], **form.cleaned_data)
        })

    def form_invalid(self, form, time_form):
        return self.render_to_response({
            'form': form,
            'time_form': time_form,
        })

    def render_to_response(self, context):
        context['time_table'] = get_time_table()
        return super().render_to_response(context)


class CourseView(DetailView):
    template_name = 'course.html'
    queryset = Course.objects.filter(semester_entry__ready=True)

    def get_object(self):
        queryset = self.get_queryset()

        no = self.kwargs['no']

        return get_object_or_404(
            queryset,
            no=no,
        )

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
