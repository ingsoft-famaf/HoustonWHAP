from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse as HTTPr
from ..models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

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
        name = req.POST['name']
        description = req.POST.get('description', '')
        deadline = None if req.POST.get('deadline', '') == '' else req.POST.get('deadline')
        notify_user = True if req.POST.get('notify_user', False) else False
        req.user.category_set.get(id=category).task_set.get(id=task).subtask_set.create(name=name, description=description, deadline=deadline, notify_user=notify_user, complete=False)
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

        subtask = req.user.category_set.get(id=category).task_set.get(id=task).subtask_set.get(id=subtask)
        subtask.name = req.POST.get('new_name', subtask.name)
        subtask.description = req.POST.get('new_description', subtask.description)
        subtask.deadline = req.POST.get('new_deadline', subtask.deadline)
        subtask.notify_user = bool(req.POST.get('new_notify_user', subtask.notify_user))
        subtask.complete = bool(req.POST.get('complete', subtask.complete))
        subtask.save()
        return redirect('subtask', category=category, task=task)

class SubTaskDeleteView(LoginRequiredMixin, View):
    def post(self, req, category, task, subtask):
        req.user.category_set.get(id=category).task_set.get(id=task).subtask_set.get(id=subtask).delete()
        return redirect('subtask', category=category, task= task)
