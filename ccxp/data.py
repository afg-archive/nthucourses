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
            ) = tag.text.split(None, 1) + [None]
