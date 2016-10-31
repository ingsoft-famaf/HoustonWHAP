from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse as HTTPr
from ..models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
        data = _validate_task_deadline(data)

        req.user.category_set.get(id=category) \
            .task_set.create(name=data['name'], \
                             description=data['description'], \
                             deadline=data['deadline'], \
                             notify_user=data['notify_user'], \
                             complete=False)

        return redirect('task', category=category)

class TaskEditView(LoginRequiredMixin, View):
    def post(self, req, category, task):
        data = _task_data_from_POST(req.POST)
        data = _validate_task_deadline(data)

        task = req.user.category_set.get(id=category).task_set.get(id=task)

        task.name = data['name']
        task.description = data['description']
        task.deadline = data['deadline']
        task.notify_user = data['notify_user']
        task.complete = data['complete']

        task.save()

        return redirect('task', category=category)

class TaskDeleteView(LoginRequiredMixin, View):
    def post(self, req, category, task):
        req.user.category_set.get(id=category).task_set.get(id=task).delete()
        return redirect('task', category=category)

def _task_data_from_POST(post):
    result = {
        'name': post.get('name', ''),
        'description': post.get('description', ''),
        'notify_user': True if post.get('notify_user', False) else False,
        'deadline': None if post.get('deadline', None) == '' else post.get('deadline'),
        'complete': True if post.get('complete', False) else False
    }
    
    # Check semantics
    if result['notify_user'] and (result['deadline'] is not None):
        try:
            result['deadline'] = parse_datetime(result['deadline'])
            if result['deadline'] is not None:
                result['deadline'] = timezone.make_aware(result['deadline'])
            else:
                result['notify_user'] = False
        except ValueError:
            result['notify_user'] = False
            result['deadline'] = None
    else:
        result['notify_user'] = False
        result['deadline'] = None

    return result

def _validate_task_deadline(task):
    if task['notify_user'] and task['deadline'] < timezone.now():
        print 'Datetime from task is invalid.'
        task['notify_user'] = False
        task['deadline'] = None
    return task
