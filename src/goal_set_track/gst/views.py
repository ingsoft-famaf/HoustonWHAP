from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse as HTTPr
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def home(req):
    viewitems = {
        'title': 'Home',
        'username': req.user.username
    }
    return redirect('category')

class LoginView(View):
    def get(self, req):
        viewitems = {
            'title': 'Login',
        }
        return render(req, 'gst/login.html', viewitems)

    def post(self, req):
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('category')
        else:
            return HTTPr('El usuario o contrasena son incorrectos.')

class LogoutView(LoginRequiredMixin, View):
    def get(self, req):
        logout(req)
        viewitems = {
            'title': 'Logout',
        }
        return render(req, 'gst/login.html', viewitems)

class RegisterView(View):
    def get(self, req):
        viewitems = {
        }
        return render(req, 'gst/register.html', viewitems)

    def post(self, req):
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        return HTTPr('Bienvenido ' + new_user.first_name + '. Esperamos que disfrutes del servicio.')

class CategoryView(LoginRequiredMixin, View):
    def get(self, req):
        viewitems = {
            'title': 'Categories',
            'username': req.user.username,
            'categories': req.user.category_set.all()
        }
        return render(req, 'gst/category.html', viewitems)

class CategoryCreateView(LoginRequiredMixin, View):
    def post(self, req):
        name = req.POST['name']
        req.user.category_set.create(name = name)
        return redirect('task', category=req.user.category_set.get(name=name).id)

class CategoryEditView(LoginRequiredMixin, View):
    def get(self, req):
        viewitems = {
        }
        categorys = Category.objects.filter(user = u)
        return render(req, 'gst/category_delete.html', {'categorys': categorys, 'edit':True})

    def post(self, req):
        oldName = req.POST['oldName']
        newName = req.POST['newName']
        Category.objects.filter(name=oldName).filter(user=u).update(name=newName)
        return HTTPr('Successful edited the category')

class CategoryDeleteView(LoginRequiredMixin, View):
    def get(self, req):
        viewitems = {
        }
        categorys = Category.objects.filter(user = u)
        return render(req, 'gst/category_delete.html', {'categorys': categorys})

    def post(self, req):
        n = req.POST['name']
        Category.objects.filter(name=n).filter(user=u).delete()
        return HTTPr('Successful deleted category')

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
    def get(self, req):
        viewitems = {
        }
        return render(req, 'task/task_delete.html', viewitems)

    def post(self, req):
        t = SubTask.objects.get(name=req.POST['name'])
        t.delete()
        return HTTPr('Deleted.')

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
    def post(self, req, category, task, subtask):
        subtask = req.user.category_set.get(id=category).task_set.get(id=task).subtask_set.get(pk=subtask)
        subtask.name = req.POST.get('new_name', subtask.name)
        subtask.description = req.POST.get('description', subtask.description)
        subtask.deadline = req.POST.get('deadline', subtask.deadline)
        subtask.notify_user = req.POST.get('notify_user', subtask.notify_user)
        subtask.complete = bool(req.POST.get('complete', subtask.complete))
        subtask.save()
        return redirect('subtask', category=category, task=task)

class SubTaskDeleteView(LoginRequiredMixin, View):
    def get(self, req):
        viewitems = {
        }
        subtasks = SubTask.objects.filter(user=req.user)
        return render(req, 'gst/sub_task_delete.html', {'subtasks': subtasks})

    def post(self, req):
        n = req.POST['name']
        SubTask.objects.filter(name=n).filter(user=req.user).delete()
        return HTTPr('Successful deleted sub task.')
