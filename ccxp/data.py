import re


def xpath1(element, xpath):
    result = element.xpath(xpath)
    assert len(result) == 1, 'got %d elements from %s' % (len(element), xpath)
    return result[0]


def extract_div(element):
    result = element.xpath('div')
    assert len(result) == 1
    return result[0].text_content().strip()


def extract_multirow(element, count=None):
    result = [s.strip() for s in element.itertext()]
    if count is not None:
        result += [''] * (count - len(result))
    return result


class Semester(dict):
    def __init__(self, tag):
        self['value'] = tag.attrib['value']
        self['year'], self['section'] = map(
            int, tag.attrib['value'].split('|'))
        self['name'] = tag.text.strip()


class Department(dict):
    def __init__(self, tag):
        try:
            (
                self['abbr'],
                self['name_zh'],
                self['name_en']
            ) = tag.text.split(None, 2)
        except ValueError:
            (
                self['abbr'],
                self['name_zh'],
                self['name_en']
            ) = tag.text.split(None, 1) + ['']


class Course(dict):
    def __init__(self, row, footer):
        tds = row.xpath('td')
        assert len(tds) == 12, '%d != 12' % len(tds)
        self['no'] = extract_div(tds[0])
        (
            self['title_zh'],
            self['title_en'],
            self['ge_line'],
        ) = extract_multirow(tds[1], 3)
        self['credit'] = int(extract_div(tds[2]))
        self['time'] = extract_div(tds[3])
        rc = list(filter(None, extract_multirow(
            tds[4].xpath('div/a')[0],
            2)))
        if rc:
            self['room'], capacity = rc[:2]  # TODO
            self['capacity'] = int(capacity.partition('容量')[-1])
        else:
            self['room'] = ''
            self['capacity'] = None
        self['teacher'] = extract_div(tds[5])
        size_limit_str = extract_div(tds[6])
        if size_limit_str:
            (
                size_limit_str, _, freshmen_reserved
            ) = size_limit_str.rstrip('人').partition('大一新生保留')
            self['size_limit'] = int(size_limit_str)
        else:
            self['size_limit'] = self['freshmen_reserved'] = None
        self['note'] = '\n'.join(filter(None, extract_multirow(tds[7])))
        self['enrollment'] = int(extract_div(tds[8]))
        self['object'] = extract_div(tds[9])
        self['prerequisite'] = extract_div(tds[10])
        self['required_by'] = extract_div(footer.xpath('td')[0])


class Syllabus(dict):
    syllabus_pattern = re.compile(r'\n{4,}')
    def __init__(self, document):
        self['no'] = xpath1(
            document,
            '/html/body/div/table[1]/tr[2]/td[2]').text
        self['credit'] = int(xpath1(
            document,
            '/html/body/div/table[1]/tr[2]/td[4]').text)
        self['title_zh'] = xpath1(
            document,
            '/html/body/div/table[1]/tr[3]/td[2]').text.strip()
        self['title_en'] = xpath1(
            document,
            '/html/body/div/table[1]/tr[4]/td[2]').text.strip()
        self['teacher'] = xpath1(
            document,
            '/html/body/div/table[1]/tr[5]/td[2]').text.strip()
        self['time'] = xpath1(
            document,
            '/html/body/div/table[1]/tr[6]/td[2]').text.strip()
        self['room'] = xpath1(
            document,
            '/html/body/div/table[1]/tr[6]/td[4]').text.strip()
        syllabus = extract_multirow(xpath1(
            document,
            '/html/body/div/table[4]/tr[2]/td'))
        self['syllabus'] = self.syllabus_pattern.sub(
            '\n\n\n',
            '\n'.join(syllabus))
