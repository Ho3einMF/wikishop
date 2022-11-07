from django.core.management.base import BaseCommand

from apps.content.tests.factories import PostFactory


class Command(BaseCommand):
    help = 'Creates Fake Posts'

    def add_arguments(self, parser):
        parser.add_argument('size', type=int, help='Indicates the number of posts to be created')

    def handle(self, *args, **kwargs):
        PostFactory.create_batch(kwargs['size'])
        self.stdout.write(f'{kwargs["size"]} posts(s) created.')
