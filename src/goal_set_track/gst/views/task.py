from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse as HTTPr
from ..models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

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
        name = req.POST['name']
        description = req.POST.get('description', '')
        deadline = None if req.POST.get('deadline', '') == '' else req.POST.get('deadline')
        notify_user = True if req.POST.get('notify_user', False) else False
        req.user.category_set.get(id=category).task_set.create(name=name, description=description,
                                                                      deadline=deadline, notify_user=notify_user,
                                                                      complete=False)
        return redirect('task', category=category)

class TaskEditView(LoginRequiredMixin, View):
    def post(self, req, category, task):
        task = req.user.category_set.get(id=category).task_set.get(id=task)
        task.name = req.POST.get('new_name', task.name)
        task.description = req.POST.get('description', task.description)
        task.deadline = req.POST.get('deadline', task.deadline)
        task.notify_user = req.POST.get('notify_user', task.notify_user)
        task.complete = bool(req.POST.get('complete', task.complete))
        task.save()
        return redirect('task', category=category)

class TaskDeleteView(LoginRequiredMixin, View):
    def post(self, req, category, task):
        req.user.category_set.get(id=category).task_set.get(id=task).delete()
        return redirect('task', category=category)
