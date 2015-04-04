from django import forms

from courses.models import Semester, Department


class CourseForm(forms.Form):
    semester = forms.ChoiceField(
        choices=[
            (semester.value, semester.name)
            for semester in Semester.objects.filter(ready=True)
        ]
    )

    departments = forms.ChoiceField(
        choices=[
            (
                department.abbr,
                '{} {}'.format(department.abbr, department.name_zh)
            )
            for department in Department.objects.all()
        ]
    )
