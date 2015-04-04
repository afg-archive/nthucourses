from django import forms

from courses.models import Semester, Department


class CourseForm(forms.Form):
    semester = forms.ChoiceField(
        choices=[
            (semester.pk, semester.name)
            for semester in Semester.objects.filter(ready=True)
        ]
    )

    departments = forms.ChoiceField(
        choices=[
            (
                department.pk,
                '{} {}'.format(department.abbr, department.name_zh)
            )
            for department in Department.objects.all()
        ]
    )
