from time import sleep

from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from celery import shared_task


@shared_task(bind=True)
def testing_celery_task(self):
    sleep(20)
    user_count = User.objects.count()
    User.objects.create(
        username=f'test{user_count}',
        email=f'email{user_count}@gmail.com',
        password='<PASSWORD>',
    )

