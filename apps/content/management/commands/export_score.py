import os

from django.core.management.base import BaseCommand
from django_pandas.io import read_frame

from apps.content.conf import SCORE_EXPORT_DIRECTORY
from apps.content.models import Score


class Command(BaseCommand):
    help = 'Exports Score Table'

    def handle(self, *args, **kwargs):
        queryset = Score.objects.all()
        dataframe = read_frame(queryset, fieldnames=['id', 'score', 'user__id', 'post__id'])

        if not os.path.exists(SCORE_EXPORT_DIRECTORY):
            os.mkdir(SCORE_EXPORT_DIRECTORY)

        dataframe.to_csv(f'{SCORE_EXPORT_DIRECTORY}/score.csv')
        self.stdout.write('score csv file created in the data directory.')
