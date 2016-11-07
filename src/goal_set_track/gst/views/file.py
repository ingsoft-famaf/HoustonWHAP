from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse as HTTPr
from ..models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from deadline import number_deadlines_from_user

class FileView(LoginRequiredMixin, View):
    def get(self, req, category, task):
        viewitems = {
            'title': 'Attached files',
            'username': req.user.username,
            'category': req.user.category_set.get(id=category),
            'task': req.user.category_set.get(id=category).task_set.get(id=task),
            'files': req.user.category_set.get(id=category).task_set.get(id=task).file_set.all(),
        }
        return render(req, 'gst/file.html', viewitems)

class FileAddView(LoginRequiredMixin, View):
    def post(self, req, category, task):

        t = req.user.category_set.get(id=category).task_set.get(id=task)
        t.file_set.create(name=req.POST['name'], file=req.POST['file'])

        return redirect('file', category=category, task=task)

class FileDeleteView(LoginRequiredMixin, View):
    def post(self, req, category, task, file):
        req.user.category_set.get(id=category).task_set.get(id=task).file_set.get(id=file).delete()
    
        return redirect('file', category=category, task=task)


class FileDowloadView(LoginRequiredMixin, View):
    def post(self, req, category, task, file):
        print "\n\n\nBBBBBBBBBB\n\n\n"

#        return redirect('file', category=category, task=task)
