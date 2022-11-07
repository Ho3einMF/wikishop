from django.core.management.base import BaseCommand

from apps.accounts.tests.factories import UserFactory


class Command(BaseCommand):
    help = 'Creates Fake Users'

    def add_arguments(self, parser):
        parser.add_argument('size', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        UserFactory.create_batch(kwargs['size'])
        self.stdout.write(f'{kwargs["size"]} user(s) created.')
