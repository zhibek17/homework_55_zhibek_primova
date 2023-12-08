from django.urls import path
from .views import *

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task/<int:pk>/', task_view, name='task_view'),
    path('add/', task_add, name='task_add'),
    path('task/<int:pk>/update', task_update, name='task_update'),
    path('task/<int:pk>/delete', task_delete, name='task_delete'),
]
