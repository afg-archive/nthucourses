import operator

from courses.models import Semester, Department, Course
from ccxp.fetch import Browser


def get_browser(browser=None):
    if browser is None:
        browser = Browser()
        print(browser.get_captcha_url())
        browser.set_captcha(input('Input captcha from above url: '))
    return browser


def update_departments(browser=None):
    if browser is None:
        browser = Browser()
    new = update = 0
    for department in browser.get_departments():
        if Department.objects.filter(abbr=department['abbr']).exists():
            dbdep = Department.objects.get(abbr=department['abbr'])
            dbdep.name_zh = department['name_zh']
            dbdep.name_en = department['name_en']
            update += 1
        else:
            Department.objects.create(**department)
            new += 1
    print(new, 'departments created,', update, 'updated.')


def update_semesters(browser=None):
    if browser is None:
        browser = Browser()
    new = update = 0
    for semester in browser.get_semesters():
        if Semester.objects.filter(value=semester['value']).exists():
            dbsem = Semester.objects.get(value=semester.pop('value'))
            for key, value in semester.items():
                setattr(dbsem, key, value)
            update += 1
        else:
            Semester.objects.create(**semester)
            new += 1
    print(new, 'semesters created,', update, 'updated.')


def update_semester(browser=None, semester_code=None):
    browser = get_browser(browser)
    update_departments(browser)
    if semester_code is not None:
        browser.set_semester(semester_code)
        update_semesters(browser)
    browser_semester = browser.get_current_semester()
    print(browser_semester)
    semester = Semester.objects.get(value=browser_semester['value'])
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
    for n, course in enumerate(courses.values(), start=1):
        syllabus_data = browser.get_syllabus(course['no'])
        course.update(filter(operator.itemgetter(1), syllabus_data.items()))
        print(
            'Collecting syllabus from',
            course['no'],
            '...',
            n,
            end='\r')
    print()
    semester_entry = semester.semesterentry_set.create()
    try:
        for n, course in enumerate(courses.values(), start=1):
            semester_entry.course_set.create(**course)
            print('Updating courses', '...', n, end='\r')
        print()
        for n, (department, course_nos) in enumerate(departments.items()):
            courses = semester_entry.course_set.filter(no__in=course_nos)
            ThroughModel = Course.departments.through
            ThroughModel.objects.bulk_create(
                ThroughModel(
                    department=Department.objects.get(abbr=department),
                    course=course,
                )
                for course in courses
            )
            print('Updating department data', '...', n, end='\r')
        print()
        semester_entry.ready = True
        semester_entry.save()
    except:
        semester_entry.delete()
        raise
    else:
        semester.semesterentry_set.filter(
            semester=semester).exclude(
            pk=semester_entry.pk).delete()
    return browser


def update_targets(semesters):
    browser = get_browser()
    update_departments(browser)
    update_semesters(browser)
    for semester in semesters:
        update_semester(browser, semester.value)


def get_viable_targets():
    return Semester.objects.exclude(section=30)


def update_latest():
    update_targets(get_viable_targets()[:2])


def update_recent():
    update_targets(get_viable_targets()[:5])
