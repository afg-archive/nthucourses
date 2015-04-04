from courses.models import Semester, Department
from ccxp.fetch import Browser


def update_departments():
    new = update = 0
    for department in Browser().get_departments():
        if Department.objects.filter(abbr=department['abbr']).exists():
            dbdep = Department.objects.get(abbr=department['abbr'])
            dbdep.name_zh = department['name_zh']
            dbdep.name_en = department['name_en']
            update += 1
        else:
            Department.objects.create(**department)
            new += 1
    print(new, 'departments created,', update, 'updated.')


def update_semester(browser=None, semester_code=None):
    if browser is None:
        browser = Browser()
        print(browser.get_captcha_url())
        browser.set_captcha(input('Input captcha from above url: '))
    if semester_code is not None:
        browser.set_semester(semester_code)
    browser_semester = browser.get_current_semester()
    print(browser_semester)
    departments = dict()
    courses = dict()
    for department in Department.objects.all():
        cbd = browser.get_courses_by_department(department.abbr)
        departments[department.abbr] = [c['no'] for c in cbd]
        courses.update((c['no'], c) for c in cbd)
        print(
            'Collecting courses from',
            format(department.abbr, '4'),
            '...',
            len(courses),
            end='\r')
    print()
    semester = Semester.objects.create(**browser_semester)
    try:
        for n, course in enumerate(courses.values()):
            semester.course_set.create(**course)
            print('Updating courses', '...', n, end='\r')
        print()
        semester.ready = True
        semester.save()
    except:
        semester.delete()
        raise
    else:
        Semester.objects.filter(
            value=semester.value).exclude(
            pk=semester.pk).delete()
