from django import forms

from courses.models import Semester, Department


class CourseForm(forms.Form):
    semester = forms.ChoiceField(choices=())
    departments = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['semester'].choices = [
            (semester.value, semester.name)
            for semester in Semester.objects.filter(ready=True)
        ]

        self.fields['departments'].choices=[
            (
                department.abbr,
                '{} {}'.format(department.abbr, department.name_zh)
            )
            for department in Department.objects.all()
        ]
