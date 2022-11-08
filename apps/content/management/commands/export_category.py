import os

from django.core.management.base import BaseCommand
from django_pandas.io import read_frame

from apps.content.conf import CATEGORY_EXPORT_DIRECTORY
from apps.content.models import Category


class Command(BaseCommand):
    help = 'Exports Category Table'

    def handle(self, *args, **kwargs):
        queryset = Category.objects.all()
        dataframe = read_frame(queryset)

        if not os.path.exists(CATEGORY_EXPORT_DIRECTORY):
            os.mkdir(CATEGORY_EXPORT_DIRECTORY)

        dataframe.to_csv(f'{CATEGORY_EXPORT_DIRECTORY}/category.csv')
        self.stdout.write('category csv file created in the data directory.')
