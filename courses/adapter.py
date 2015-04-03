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


def update_semester(semester_code):
    browser = Browser()
    update_departments()
    print(browser.get_captcha_url())
    browser.set_captcha(input('Input captcha from above url: '))
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
