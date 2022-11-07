from django.core.management.base import BaseCommand

from apps.content.tests.factories import CategoryFactory


class Command(BaseCommand):
    help = 'Creates Fake Categories'

    def add_arguments(self, parser):
        parser.add_argument('size', type=int, help='Indicates the number of categories to be created')

    def handle(self, *args, **kwargs):
        CategoryFactory.create_batch(kwargs['size'])
        self.stdout.write(f'{kwargs["size"]} categories(s) created.')
