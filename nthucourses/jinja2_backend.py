from django.template.backends import jinja2
from django.template import Context


class Jinja2(jinja2.Jinja2):
    def get_template(self, template_name):
        return Template(self.env.get_template(template_name))


class Template(jinja2.Template):
    def render(self, context=None, request=None):
        print(context)
        if isinstance(context, Context):
            context = context.flatten()
        return super().render(context=context, request=request)
