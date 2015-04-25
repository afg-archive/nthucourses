from django.core.management.base import BaseCommand

import sys

from courses import adapter
from logs.models import Logger

class Command(BaseCommand):
    help = 'update stuff'

    def add_arguments(self, parser):
        parser.add_argument('section', choices=('latest', 'recent'))

    def handle(self, *args, **options):
        with Logger(' '.join(sys.argv[1:])):
            if options['section'] == 'latest':
                adapter.update_latest()
            else:
                adapter.update_recent()
