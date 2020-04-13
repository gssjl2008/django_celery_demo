# encoding: utf-8
#@author: wuxing
#@file: tasks.py
#@time: 2020/4/13 10:54
#@desc:

from celery.task import Task
from time import sleep


class Celery_demo_tasks(Task):

    name = 'dj_celery_demo'

    def run(self, *args, **kwargs):
        print(f"task start...")
        sleep(3)
        print(f"args:{args}, kwargs: {kwargs}")
        print(f"task end...")