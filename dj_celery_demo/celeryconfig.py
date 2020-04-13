# encoding: utf-8
#@author: wuxing
#@file: celeryconfig.py
#@time: 2020/4/13 10:53
#@desc:

from datetime import timedelta
# 导入 djcelery
import djcelery
djcelery.setup_loader()

BROKER_BACKEND = 'redis'
BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'

# 配置任务
CELERY_IMPORTS = {
    'celery_demo.tasks',
}

# 设置多条任务队列，
CELERY_QUEUES = {
    'beat_tasks': {
        'exchange': 'beat_tasks',
        'exchange_type': 'direct',
        'binding_key': 'beat_tasks'
    },
    'work_tasks': {
        'exchange': 'work_tasks',
        'exchange_type': 'direct',
        'binding_key': 'work_tasks'
    }
}

# 默认queue
CELERY_DEFAULT_QUEUE = 'work_tasks'

#  某些情况可以防止死锁
CELERY_FORCE_EXECV = True

# 设置并发worker进程
CELERY_CONCURRENCY = 4

# 允许重试
CELERY_ACKS_LATE = True

# 每个worker最多执行100个任务被销毁， 防止内存泄露
CELERY_MAX_TASKS_PER_CHILD = 100

# 单个任务最大运行时间， 超过则被kill
CELERY_TASK_TIME_LIMIT = 12 * 30

# 配置定时任务
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'dj_celery_demo',
        'schedule': timedelta(seconds=10),
        'args': (1,10,100,),
        'options': {
            'queue': 'beat_tasks'
        }
    }
}
