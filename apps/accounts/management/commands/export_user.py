import os

from django.core.management.base import BaseCommand
from django_pandas.io import read_frame

from apps.accounts.conf import USER_EXPORT_DIRECTORY
from apps.accounts.models import User


class Command(BaseCommand):
    help = 'Exports User Table'

    def handle(self, *args, **kwargs):
        queryset = User.objects.all()
        dataframe = read_frame(queryset, fieldnames=['id', 'username', 'first_name', 'last_name', 'email'])

        if not os.path.exists(USER_EXPORT_DIRECTORY):
            os.mkdir(USER_EXPORT_DIRECTORY)

        dataframe.to_csv(f'{USER_EXPORT_DIRECTORY}/user.csv')
        self.stdout.write('user csv file created in the data directory.')
