from urllib.parse import urljoin

import requests
from lxml.html import fromstring

from ccxp.data import Semester, Department, Course, Syllabus, xpath1


index_url = 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/6/6.2/6.2.9/JH629001.php'  # noqa
syllabus_url = 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/common/Syllabus/1.php'  # noqa
encoding = 'cp950'


class Browser:
    def __init__(self, frozen=None):
        self.session = requests.Session()
        self.index = self.get_index()
        self.form = self.xpath1('/html/body/div/form')
        self.ACIXSTORE = xpath1(self.form, 'input[@name="ACIXSTORE"]')
        self.captcha = self.xpath1('/html/body/div/form/table[2]/tr/td/input')
        if frozen is not None:
            self.ACIXSTORE.value = frozen['ACIXSTORE']
            self.captcha.value = frozen['captcha']

    def xpath1(self, xpath):
        return xpath1(self.index, xpath)

    def get_index(self):
        response = self.session.get(index_url)
        response.encoding = encoding
        return fromstring(response.text, base_url=index_url)

    def handle_select(self, type_, xpath):
        select = self.xpath1(xpath)
        return [
            type_(option)
            for option
            in select.xpath('option')
            if option.attrib.get('value')]

    def set_semester(self, semester):
        select = self.xpath1('//*[@id="YS_id"]')
        select.value = semester

    def get_semesters(self):
        return self.handle_select(Semester, '//*[@id="YS_id"]')

    def get_current_semester(self):
        select = self.xpath1('//*[@id="YS_id"]')
        for semester in self.get_semesters():
            if select.value == semester['value']:
                return semester

    def get_departments(self):
        return self.handle_select(
            Department,
            '/html/body/div/form/table[1]/tr[4]/td/select')

    def get_department_html(self, value):
        select = self.xpath1('/html/body/div/form/table[1]/tr[4]/td/select')
        select.value = value
        form = xpath1(self.index, '/html/body/div/form')
        response = self.submit_form(form)
        response.encoding = encoding
        return response.text

    def get_courses_by_department(self, value):
        document = fromstring(
            self.get_department_html(value),
            base_url=index_url)
        trs = document.xpath(
            '/html/body/div/form/table/tr[contains(@class, "class3")]')
        assert not (len(trs) % 2), len(trs)
        return [
            Course(*args)
            for args
            in zip(trs[::2], trs[1::2])
        ]

    def get_captcha_url(self):
        img = self.xpath1('/html/body/div/form/table[2]/tr/td/img')
        return urljoin(index_url, img.attrib['src'])

    def set_captcha(self, code):
        self.captcha.value = code

    def submit_form(self, form):
        values = form.form_values() + [('cond', 'a')]
        url = form.action
        return self.session.post(url, data=values)

    def get_syllabus_html(self, course):
        response = self.session.get(
            syllabus_url,
            params=dict(ACIXSTORE=self.ACIXSTORE.value, c_key=course)
        )
        response.encoding = encoding
        return response.text

    def get_syllabus(self, course):
        return Syllabus(fromstring(self.get_syllabus_html(course)))

    def freeze(self):
        return {
            'ACIXSTORE': self.ACIXSTORE.value,
            'captcha': self.captcha.value,
        }
