from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View
from deadline import is_deadline_near
from django.utils import timezone

def created_tasks_from_user(user):
    created_tasks = []
    for category in user.category_set.all():
        for task in category.task_set.all():
            if task.created_at.month == timezone.now().month:
                created_tasks.append(task)

def completed_tasks_from_user(user):
    completed_tasks = []
    for category in user.category_set.all():
        for task in category.task_set.all():
            if task.complete and task.created_at.month == timezone.now().month:
                completed_tasks.append(task)

def failed_tasks_from_user(user):
    failed_tasks = []
    for category in user.category_set.all():
        for task in category.task_set.all():
            if not task.complete and is_deadline_near(task.deadline) and task.created_at.month == timezone.now().month:
                failed_tasks.append(task)

class StatisticsView(LoginRequiredMixin, View):
    def get(self, req):
        created_tasks = created_tasks_from_user(req.user)
        completed_tasks = completed_tasks_from_user(req.user)
        failed_tasks = failed_tasks_from_user(req.user)
        viewitems = {
            'title': 'Statistics',
            'username': req.user.username,
            'created_tasks': created_tasks if len(created_tasks) > 0 else False,
            'completed_tasks': completed_tasks if len(completed_tasks) > 0 else False,
            'failed_tasks': failed_tasks if len(failed_tasks) > 0 else False
        }
        return render(req, 'gst/statistics.html', viewitems)
