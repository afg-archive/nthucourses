from django.views.generic.edit import FormView

from courses.forms import CourseForm


class Course(FormView):
    template_name = 'courses.html'
    form_class = CourseForm
