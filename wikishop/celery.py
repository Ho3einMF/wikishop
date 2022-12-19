import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wikishop.settings')

app = Celery('wikishop')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'clean_sessions': {
        'task': 'apps.accounts.tasks.clean_sessions',
        'schedule': crontab(hour='*/24')
    }
}
