from django import forms

from courses.models import SemesterEntry, Department


class CourseForm(forms.Form):
    semester = forms.ChoiceField(choices=())
    departments = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['semester'].choices = [
            (semester_entry.semester.value, semester_entry.semester.name)
            for semester_entry
            in SemesterEntry.objects.filter(ready=True)
        ]

        self.fields['departments'].choices = [
            (
                department.abbr,
                '{} {}'.format(department.abbr, department.name_zh)
            )
            for department in Department.objects.all()
        ]
