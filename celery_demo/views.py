from django.shortcuts import render, Http404, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.template import loader
from celery_demo.tasks import Celery_demo_tasks
from .models import Question

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
    # return JsonResponse({"result":"Test"})
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list,}
    return render(request, 'index.html', context)
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render(context, request))

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def result(request, question_id):
    reponse = "Yor're looking at the result of question %s." 
    return HttpResponse(reponse %question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)
