from courses.models import Department
from ccxp.fetch import Browser


def update_departments():
    count = 0
    for department in Browser().get_departments():
        obj, created = Department.objects.get_or_create(**department)
        count += created
    print(count, 'departments created.')
