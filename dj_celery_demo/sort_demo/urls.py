# encoding: utf-8
#@author: wuxing
#@file: urls.py
#@time: 2020/4/17 10:41
#@desc:

from .views import *
from django.urls import path

app_name="sort"
urlpatterns = [
    path('index/', index, name='index'),
    # path('do/', do, name='do')
]