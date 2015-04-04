import json

from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from django.utils.html import format_html, mark_safe
from django.utils.timezone import localtime

from jinja2 import Environment

from bootstrap3.forms import render_form


def navli(url, display, active=False, current=None, disabled=False):
    if current is not None:
        active = current == url
    classes = []
    if active:
        classes.append('active')
    if disabled:
        classes.append('disabled')
    return format_html(
        '<li class="{classes}"><a href="{url}">{display}</a></li>',
        classes=' '.join(classes),
        url=url,
        display=display,
    )


def localftime(time):
    return localtime(time).strftime('%Y/%m/%d %H:%M:%S')


def safe_rendering(renderer):
    def safe_renderer(*args, **kwargs):
        return mark_safe(renderer(*args, **kwargs))
    return safe_renderer


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'navli': navli,
        'localtime': localtime,
        'localftime': localftime,
        'render_form': safe_rendering(render_form),
        'json': safe_rendering(json.dumps),
    })
    return env
