from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def task_list(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'task_list.html', {'tasks': tasks})


def task_view(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, 'task_view.html', {'task': task})


def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task_list'))
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})
