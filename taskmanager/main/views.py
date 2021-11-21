from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    attrs = {
        'title': 'Главная страница сайта',
        'tasks': tasks,
        'link_style_index': 'text-white'
    }
    return render(request, 'main/index.html', attrs)


def about(request):
    attrs = {
        'title': 'Страница про нас',
        'link_style_about': 'text-white'
    }
    return render(request, 'main/about.html', attrs)


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task:home')
        else:
            error = 'Форма неверна'

    form = TaskForm()
    attrs = {
        'title': 'Добавление задачи',
        'link_style_create': 'text-white',
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', attrs)


def edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:home')
        else:
            error = 'Форма неверна'

    form = TaskForm(instance=task)
    context = {
        'title': 'Редактирование задачи',
        'form': form,
        'error': error,
        'task': task
    }
    return render(request, 'main/create.html', context)


def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task:home')
    else:
        return render(request, 'main/delete.html', {'task': task})
