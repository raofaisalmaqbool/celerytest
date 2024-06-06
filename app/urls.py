from django.urls import path

from app.views import testing_celery

urlpatterns = [

    path('test', testing_celery, name='testing_celery'),

    ]