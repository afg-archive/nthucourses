from __future__ import print_function

import logging
import subprocess
import tempfile

import lxml.html
import requests


logger = logging.getLogger(__name__)

form_url = 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/6/6.2/6.2.9/JH629001.php'  # noqa
syllabus_url = 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/6/6.2/6.2.9/JH629002.php'  # noqa
captcha_url_base = 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/mod/auth_img/auth_img.php'  # noqa


class DecaptchaFailure(Exception):
    pass


def tesseract(path):
    return subprocess.check_output([
        'tesseract',
        path, '-',
        '-psm', '8',
        '-c', 'tessedit_char_whitelist=0123456789', 'nobatch'
    ]).strip()


def decaptcha_url(url):
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmpimg:
        tmpimg.write(requests.get(url).content)
        tmpimg.flush()
        return tesseract(tmpimg.name).replace(b' ', b'')


def get_acixstore():
    response = requests.get(form_url)
    response.encoding = 'cp950'
    document = lxml.html.fromstring(response.text)
    return document.xpath('//input[@name="ACIXSTORE"]')[0].value


def get_captcha_url(acixstore):
    return '%s?ACIXSTORE=%s' % (captcha_url_base, acixstore)


def validate_by_post(acixstore, captcha):
    response = requests.post(
        syllabus_url,
        data={
            'ACIXSTORE': acixstore,
            'YS': '103|30',
            'auth_num': captcha,
        }
    )
    if b'<html>' in response.content:
        logger.debug('%r: %r is correct', acixstore, captcha)
        return True
    elif b'interrupted' in response.content:
        logger.debug(
            '%r: %r session is interrupted', acixstore, captcha)
        return False
    logger.debug('%r: %r is simply incorrect', acixstore, captcha)
    return False


def validate(acixstore, captcha):
    if not captcha.isdigit():
        logger.debug('%r: %r is not a number', acixstore, captcha)
        return False
    if not len(captcha) == 3:
        logger.debug('%r: %r does not have length == 3', acixstore, captcha)
        return False
    return validate_by_post(acixstore, captcha)


def get_pair(retries=32):
    for try_ in range(retries):
        acixstore = get_acixstore()
        captcha = decaptcha_url(get_captcha_url(acixstore))
        if validate(acixstore, captcha):
            return acixstore, captcha
    raise DecaptchaFailure('Cannot decaptcha, retries=%i' % retries)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Get a acixstore-captcha pair from ccxp course index')

    parser.add_argument(
        '--retries',
        help='max retries',
        default=32,
        type=int)
    parser.add_argument(
        '--quiet',
        help="don't log",
        action='store_true',
    )

    args = parser.parse_args()

    if not args.quiet:
        logger.setLevel(logging.DEBUG)
        logger.addHandler(logging.StreamHandler())

    print(get_pair(args.retries))
