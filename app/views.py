from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.tests import testing_celery_task

# Create your views here.
@csrf_exempt
def testing_celery(request):
    testing_celery_task.apply_async()
    return JsonResponse({'status': 'ok'})