from django.urls import path
from .views import *

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task/<int:task_id>/', task_view, name='task_view'),
    path('add/', task_add, name='task_add'),
]
