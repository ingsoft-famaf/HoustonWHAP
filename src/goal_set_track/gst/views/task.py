from django.shortcuts import render, redirect
from django.views.generic import View
from ..models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.dateparse import parse_datetime
from django.utils import timezone

class TaskView(LoginRequiredMixin, View):
    def get(self, req, category):
        viewitems = {
            'title': 'Tareas',
            'username': req.user.username,
            'category': req.user.category_set.get(id=category),
            'tasks': req.user.category_set.get(id=category).task_set.all()
        }
        return render(req, 'gst/task.html', viewitems)

class TaskCreateView(LoginRequiredMixin, View):
    def post(self, req, category):
        data = _task_data_from_POST(req.POST)
        if 'notify_user' in data:
            data = _validate_task_deadline(data)

        print data

        req.user.category_set.get(id=category) \
            .task_set.create(name=data['name'], \
                             description=data['description'], \
                             deadline=data['deadline'] if 'deadline' in data else None, \
                             notify_user=data['notify_user'] if 'notify_user' in data else False, \
                             complete=False)

        return redirect('task', category=category)

class TaskEditView(LoginRequiredMixin, View):
    def get(self, req, category, task):
        viewitems = {
            'title': 'Editar Subtarea',
            'username': req.user.username,
            'category': req.user.category_set.get(id=category),
            'task': req.user.category_set.get(id=category).task_set.get(id=task),
        }
        return render(req, 'gst/task_edit.html', viewitems)

    def post(self, req, category, task):
        data = _task_data_from_POST(req.POST)
        if 'notify_user' in data:
            data = _validate_task_deadline(data)

        task = req.user.category_set.get(id=category).task_set.get(id=task)
        if 'name' in data:
            task.name = data['name']

        if 'description' in data:
            task.description = data['description']
        
        if 'notify_user' in data:
            task.notify_user = data['notify_user']

        if 'deadline' in data:
            task.deadline = data['deadline']

        if 'complete' in data:
            task.complete = data['complete']

        task.save()

        return redirect('task', category=category)

class TaskDeleteView(LoginRequiredMixin, View):
    def post(self, req, category, task):
        req.user.category_set.get(id=category).task_set.get(id=task).delete()
        return redirect('task', category=category)

def _task_data_from_POST(post):
    result = {}
    
    if 'name' in post:
        result['name'] = post['name']

    if 'description' in post:
        result['description'] = post['description']
    
    if 'notify_user' in post:
        result['notify_user'] = post['notify_user']

    if 'deadline' in post and post['deadline'] != '':
        result['deadline'] = post['deadline']

    if 'complete' in post:
        result['complete'] = bool(post['complete'])
    
    # Check semantics
    if 'notify_user' in result and 'deadline' in result:
        try:
            result['deadline'] = parse_datetime(result['deadline'])
            if result['deadline'] is not None:
                result['deadline'] = timezone.make_aware(result['deadline'])
            else:
                result['notify_user'] = False
        except ValueError:
            result['notify_user'] = False
            result['deadline'] = None

    return result

def _validate_task_deadline(task):
    if task['notify_user'] and task['deadline'] < timezone.now():
        print 'Datetime from task is invalid.'
        task['notify_user'] = False
        task['deadline'] = None
    return task
