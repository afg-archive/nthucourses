from django import forms

from courses.models import SemesterEntry, Department


class CourseForm(forms.Form):
    semester = forms.ChoiceField(choices=())
    departments = forms.ChoiceField(choices=())

    def __init__(self, *args, **kwargs):
        entries = SemesterEntry.objects.filter(ready=True)
        entries_notempty = entries.filter(course__isnull=False).distinct()

        if entries_notempty.exists():
            initial = kwargs.setdefault('initial', {})
            initial.setdefault(
                'semester',
                entries_notempty.first().semester.value)

        super().__init__(*args, **kwargs)

        self.fields['semester'].choices = [
            (semester_entry.semester.value, semester_entry.semester.name)
            for semester_entry in entries
        ]

        self.fields['departments'].choices = [
            (
                department.abbr,
                '{} {}'.format(department.abbr, department.name_zh)
            )
            for department in Department.objects.all()
        ]
