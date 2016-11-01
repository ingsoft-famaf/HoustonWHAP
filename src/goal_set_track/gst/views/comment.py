from django.shortcuts import render, redirect
from django.views.generic import View
from ..models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.dateparse import parse_datetime
from django.utils import timezone

class CommentView(LoginRequiredMixin, View):
    def get(self, req, category, task):
        viewitems = {
            'title': 'Comentario',
            user : req.user,
            'username': req.user.username,
            'category': req.user.category_set.get(id=category),
            'task': req.user.categoty_set.get(id=category).task_set.get(id=task),
            'comment': req.user.categoty_set.get(id=category).task_set.get(id=task).comment_set.all(),
        }
        return render(req, 'gst/comment_view.html', viewitems)

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, req, category, task):
        req.user.category_set.get(id=category).task_set.get(id=task).comment_set.create(text=data['text'])
        return redirect('task', category=category, task=task)

