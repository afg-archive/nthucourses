from django.core.management.base import BaseCommand

from courses import adapter

class Command(BaseCommand):
    help = 'update stuff'

    def add_arguments(self, parser):
        parser.add_argument('section', choices=('latest', 'recent'))

    def handle(self, *args, **options):
        if options['section'] == 'latest':
            adapter.update_latest()
        else:
            adapter.update_recent()
