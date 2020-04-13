from django.shortcuts import render
from django.http import JsonResponse
from celery_demo.tasks import Celery_demo_tasks

# Create your views here.

def do(request):
    # 执行异步任务
    print(f"start do request")
    # Celery_demo_tasks.delay()
    args = (1,2,3)
    kwargs = {"a":1, "b":2}
    Celery_demo_tasks.apply_async(args, kwargs)
    print(f"end do request")

    return JsonResponse({"result":{"args":args, "kw": kwargs}})


def index(request):
    return JsonResponse({"result":"Test"})