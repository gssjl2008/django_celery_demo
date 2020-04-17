# encoding: utf-8
#@author: wuxing
#@file: urls.py
#@time: 2020/4/17 10:33
#@desc:

from django.urls import path
from .views import do, index

app_name = "celery"
urlpatterns = [
    path('index/', index, name='index'),
    path('do/', do, name='do')
]
