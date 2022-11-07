from django.core.management.base import BaseCommand

from apps.content.tests.factories import ScoreFactory


class Command(BaseCommand):
    help = 'Creates Fake Scores'

    def add_arguments(self, parser):
        parser.add_argument('size', type=int, help='Indicates the number of posts to be scored')

    def handle(self, *args, **kwargs):
        ScoreFactory.create_batch(kwargs['size'])
        self.stdout.write(f'{kwargs["size"]} posts(s) scored.')
