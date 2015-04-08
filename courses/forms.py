from django import forms

from courses.models import SemesterEntry, Department, Time


def get_department_choices():
    return [
        (
            department.abbr,
            '{} {}'.format(department.abbr, department.name_zh)
        )
        for department in Department.objects.all()
    ]


def get_entries():
    return SemesterEntry.objects.filter(ready=True)


def get_semester_initial():
    targets = get_entries().filter(course__isnull=False).distinct()
    if targets.exists():
        return targets.first().semester.value
    else:
        return ''


def get_semester_choices():
    return [
        (semester_entry.semester.value, semester_entry.semester.name)
        for semester_entry in get_entries()
    ]


class CourseForm(forms.Form):
    semester = forms.ChoiceField(
        label='學期',
        choices=get_semester_choices,
        initial=get_semester_initial)
    departments = forms.MultipleChoiceField(
        label='開課單位',
        choices=get_department_choices,
        required=False)
    teacher = forms.CharField(label='教師', required=False)
    title = forms.CharField(label='名稱', required=False)
    timeoperation = forms.ChoiceField(
        [('exclude', '搜尋選取時段以外的課'), ('in', '搜尋選取時段以內的課')],
        label='時段選項',
        initial='exclude',
        widget=forms.RadioSelect())


class TimeForm(forms.Form):
    time = forms.MultipleChoiceField(
        choices=[(time.pk, time.name) for time in Time.objects.all()],
        required=False
    )
