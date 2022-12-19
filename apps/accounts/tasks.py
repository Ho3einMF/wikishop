from celery import shared_task

from apps.accounts.models import Session


@shared_task
def clean_sessions():
    Session.objects.clean_expired_sessions()
