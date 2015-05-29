from django.core.management.base import BaseCommand

import sys

from courses import adapter
from logs.models import Logger

class Command(BaseCommand):
    help = 'update stuff'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        with Logger(' '.join(sys.argv[1:])):
            adapter.update_n(options['count'])
