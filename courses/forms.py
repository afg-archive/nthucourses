from django import forms

from courses.models import SemesterEntry, Department


class CourseForm(forms.Form):
    semester = forms.ChoiceField(label='學期', choices=())
    departments = forms.MultipleChoiceField(
        label='開課單位',
        choices=(),
        required=False)
    teacher = forms.CharField(label='教師', required=False)
    title = forms.CharField(label='名稱', required=False)
    timeoperation = forms.ChoiceField(
        [('exclude', '搜尋選取時段以外的課'), ('in', '搜尋選取時段以內的課')],
        label='時段選項',
        initial='exclude',
        widget=forms.RadioSelect())

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
