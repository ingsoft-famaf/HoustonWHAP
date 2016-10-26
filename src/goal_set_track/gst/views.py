from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse as HTTPr
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.
@login_required
def home(request):
    viewitems = {
        'title': 'Home',
        'username': request.user.username
    }
    return render(request, 'gst/index.html', viewitems)

class LoginView(View):
    def get(self, request):
        viewitems = {
            'title': 'Login',
        }
        return render(request, 'gst/login.html', viewitems)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HTTPr('Bienvenido ' + user.username)
        else:
            return HTTPr('El usuario o contrasena son incorrectos.')

class LogoutView(View):
    def get(self, request):
        logout(request)
        viewitems = {
            'title': 'Logout',
        }
        return render(request, 'gst/login.html', viewitems)

class RegisterView(View):
    def get(self, request):
        viewitems = {
        }
        return render(request, 'gst/register.html', viewitems)

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        return HTTPr('Bienvenido ' + new_user.first_name + '. Esperamos que disfrutes del servicio.')


@method_decorator(login_required, name='dispatch')
class TaskCreateView(View):
    @csrf_protect
    def get(self, request):
        viewitems = {
        }
        return render(request, 'task_create.html', viewitems)

    @csrf_protect
    def post(self, request):
        viewitems = {}
        nm = request.POST['name']
        d = request.POST['description']
        c = request.POST['category']
        cr = request.POST['created_datetime']
        dd = request.POST['deadline']
        nf = request.POST['notify_user']
        cm = request.POST['complete']
        new_task = Task.objects.create(name = nm, description = d, category = c,
             created_datetime = cr, deadline = dd, notify_user = nf, complete = cm)
        return render(request, 'gst/index.html', viewitems)

class TaskModifyView(View):
    @csrf_protect
    def get(self, request):
        viewitems = {
        }
        return render(request, 'task/task_modify.html', viewitems)

    @csrf_protect
    def post(self, request):
        t = Task.objects.get(name=request.POST['name'])
        t.name = name = request.POST['new_name']
        t.description = request.POST['description']
        t.deadline = request.POST['deadline']
        t.notify_user = request.POST['notify_user']
        t.complete = request.POST['complete']
        return HTTPr('Updated.')

@method_decorator(login_required, name='dispatch')
class TaskDeleteView(View):
    @csrf_protect
    def get(self, request):
        viewitems = {
        }
        return render(request, 'task/task_delete.html', viewitems)

    @csrf_protect
    def post(self, request):
        t = SubTask.objects.get(name=request.POST['name'])
        t.delete()
        return HTTPr('Deleted.')

#@method_decorator(login_required, name='dispatch')
class SubTaskCreateView(View):
    @csrf_protect
    def get(self, request):
        viewitems = {
        }
        return render(request, 'subtask/sub_task_create.html', viewitems)

    @csrf_protect
    def post(delf, request):
        name = request.POST['name']
        task = request.POST['task']
        deadline = request.POST['deadline']
        created_datetime = request.POST['created_datetime']
        complete = request.POST['complete']
        new_sub_task = User.objects.create(name=name, task=task,
            deadline=deadline, created_datetime=created_datetime,
            complete=complete)
        return HTTPr('Created.')

#@method_decorator(login_required, name='dispatch')
class SubTaskModifyView(View):
    @csrf_protect
    def get(self, request):
        viewitems = {
        }
        return render(request, 'subtask/sub_task_modify.html', viewitems)

    @csrf_protect
    def post(self, request):
        t = SubTask.objects.get(name=request.POST['name'])
        t.name = name = request.POST['new_name']
        t.task = request.POST['new_task']
        t.deadline = request.POST['new_deadline']
        t.complete = request.POST['new_complete']
        t.save()
        return HTTPr('Updated.')

#@method_decorator(login_required, name='dispatch')
class SubTaskDeleteView(View):
    @csrf_protect
    def get(self, request):
        viewitems = {
        }
        return render(request, 'subtask/sub_task_delete.html', viewitems)

    @csrf_protect
    def post(self, request):
        t = SubTask.objects.get(name=request.POST['name'])
        t.delete()
        return HTTPr('Deleted.')

#******************************************************
method_decorator(login_required, name='dispatch')
class CategoryCreateView(View):
    @csrf_exempt
    def get(self, request):
        viewitems = {
        }
        return render(request, 'gst/category_create.html', viewitems)

    @csrf_exempt
    def post(self, request):
        n = request.POST['name']
        u = request.user
        try:
            new_category = Category.objects.create(user = u, name = n)
            return HTTPr('Successful created category')
        except Exception as e:
            return HTTPr('You are not login.')

method_decorator(login_required, name='dispatch')
class CategoryView(View):
    @csrf_exempt
    def get(self, request):
        viewitems = {
        }
        u = request.user
        if u.is_anonymous:
            return HTTPr('You are not login.')
        else:
            categorys = Category.objects.filter(user = u)
            length = len(categorys)
            i=0
            while i<length:
                print categorys[i]
                i = i+1

            return render(request, 'gst/category.html', {'categorys': categorys})

method_decorator(login_required, name='dispatch')
class CategoryDeleteView(View):
    @csrf_exempt
    def get(self, request):
        viewitems = {
        }
        u = request.user
        if u.is_anonymous:
            return HTTPr('You are not login.')
        else:
            categorys = Category.objects.filter(user = u)
            length = len(categorys)
            i=0
            while i<length:
                print categorys[i]
                i = i+1

            return render(request, 'gst/category_delete.html', {'categorys': categorys})

    @csrf_exempt
    def post(self, request):
        n = request.POST['name']
        print "NNN = "+n
        u = request.user
        print u.username
        Category.objects.filter(name=n).filter(user=u).delete()

        return HTTPr('Successful deleted category')


method_decorator(login_required, name='dispatch')
class CategoryEditView(View):
    @csrf_exempt
    def get(self, request):
        viewitems = {
        }
        u = request.user
        if u.is_anonymous:
            return HTTPr('You are not login.')
        else:
            categorys = Category.objects.filter(user = u)
            length = len(categorys)
            i=0
            while i<length:
                print categorys[i]
                i = i+1

            return render(request, 'gst/category_delete.html', {'categorys': categorys, 'edit':True})

    @csrf_exempt
    def post(self, request):
        oldName = request.POST['oldName']
        newName = request.POST['newName']
        print "oldName = " + oldName + " newName = " + newName
        u = request.user
        print u.username

        Category.objects.filter(name=oldName).filter(user=u).update(name=newName)
        return HTTPr('Successful edited the category')