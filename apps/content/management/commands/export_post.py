import os

from django.core.management.base import BaseCommand
from django_pandas.io import read_frame

from apps.content.conf import POST_EXPORT_DIRECTORY
from apps.content.models import Post


class Command(BaseCommand):
    help = 'Exports Post Table'

    def handle(self, *args, **kwargs):
        queryset = Post.objects.all()
        dataframe = read_frame(queryset)

        if not os.path.exists(POST_EXPORT_DIRECTORY):
            os.mkdir(POST_EXPORT_DIRECTORY)

        dataframe.to_csv(f'{POST_EXPORT_DIRECTORY}/post.csv')
        self.stdout.write('post csv file created in the data directory.')
