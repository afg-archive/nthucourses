from urllib.parse import urljoin

import requests
from lxml.html import fromstring

from ccxp.data import Semester, Department, Course
from ccxp.decaptcha import decaptcha


index_url = 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/6/6.2/6.2.9/JH629001.php'  # noqa


def xpath1(element, xpath):
    result = element.xpath(xpath)
    assert len(result) == 1, 'got %d elements from %s' % (len(element), xpath)
    return result[0]


class Browser:
    def __init__(self):
        self.session = requests.Session()
        self.index = self.get_index()

    def xpath1(self, xpath):
        return xpath1(self.index, xpath)

    def get_index(self):
        response = self.session.get(index_url)
        return fromstring(response.content, base_url=index_url)

    def handle_select(self, type_, xpath):
        select = self.xpath1(xpath)
        return [
            type_(option)
            for option
            in select.xpath('option')
            if option.attrib.get('value')]

    def get_semesters(self):
        return self.handle_select(Semester, '//*[@id="YS_id"]')

    def get_departments(self):
        return self.handle_select(
            Department,
            '/html/body/div/form/table[1]/tr[4]/td/select')

    def get_department_html(self, value):
        select = self.xpath1('/html/body/div/form/table[1]/tr[4]/td/select')
        select.value = value
        form = xpath1(self.index, '/html/body/div/form')
        response = self.submit_form(form)
        response.encoding = 'big5'
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
        captcha = self.xpath1('/html/body/div/form/table[2]/tr/td/input')
        captcha.value = code

    def submit_form(self, form):
        values = form.form_values() + [('cond', 'a')]
        url = form.action
        return self.session.post(url, data=values)


if __name__ == '__main__':
    import pprint
    browser = Browser()
    browser.set_captcha(decaptcha(browser.get_captcha_url()))
    print(browser.get_courses_by_department('GE'))
