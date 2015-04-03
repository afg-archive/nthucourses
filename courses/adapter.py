from courses.models import Department
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
