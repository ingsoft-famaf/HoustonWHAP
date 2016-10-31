from django.shortcuts import render, redirect
from django.views.generic import View
from ..models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.dateparse import parse_datetime
from django.utils import timezone

class SubTaskView(LoginRequiredMixin, View):
    def get(self, req, category, task):
        viewitems = {
            'title': 'Sub Tareas',
            'username': req.user.username,
            'category': req.user.category_set.get(id=category),
            'task': req.user.category_set.get(id=category).task_set.get(id=task),
            'subtasks': req.user.category_set.get(id=category)
                            .task_set.get(id=task).subtask_set.all()
        }
        return render(req, 'gst/subtask.html', viewitems)

class SubTaskCreateView(LoginRequiredMixin, View):
    def post(self, req, category, task):
        t = req.user.category_set.get(id=category).task_set.get(id=task)
        data = _subtask_data_from_POST(req.POST)
        data = _validate_subtask_deadline(t, data)

        print data
        t.subtask_set.create(name=data['name'],
                             description=data['description'],
                             deadline=data['deadline'],
                             notify_user=data['notify_user'],
                             complete=False)

        return redirect('subtask', category=category, task=task)

class SubTaskEditView(LoginRequiredMixin, View):
    def get(self, req, category, task, subtask):
        viewitems = {
            'title': 'Editar Subtarea',
            'username': req.user.username,
            'category': req.user.category_set.get(id=category),
            'task': req.user.category_set.get(id=category).task_set.get(id=task),
            'subtask': req.user.category_set.get(id=category).task_set.get(id=task).subtask_set.get(id=subtask)
        }
        return render(req, 'gst/subtask_edit.html', viewitems)

    def post(self, req, category, task, subtask):
        task = req.user.category_set.get(id=category).task_set.get(id=task)
        data = _subtask_data_from_POST(req.POST)
        data = _validate_subtask_deadline(task, data)

        subtask = req.user.category_set.get(id=category).task_set.get(id=task).subtask_set.get(id=subtask)

        subtask.name = data['name']
        subtask.description = data['description']
        subtask.deadline = data['deadline']
        subtask.notify_user = data['notify_user']
        subtask.complete = data['complete']

        print data
        subtask.save()

        return redirect('subtask', category=category, task=task)

class SubTaskDeleteView(LoginRequiredMixin, View):
    def post(self, req, category, task, subtask):
        req.user.category_set.get(id=category).task_set.get(id=task).subtask_set.get(id=subtask).delete()
        return redirect('subtask', category=category, task=task)

def _subtask_data_from_POST(post):
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

def _validate_subtask_deadline(task, subtask):
    print subtask['deadline']
    if subtask['notify_user'] and (
        subtask['deadline'] < timezone.now() or
        subtask['deadline'] > task.deadline):
        print 'Datetime from subtask is invalid.'
        subtask['notify_user'] = False
        subtask['deadline'] = None

    print subtask
    return subtask
