from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse as HTTPr
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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
        return render(request, 'newtask.html', viewitems)

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

@login_required
class SubTaskCreateView(View):
    def get(self, request):
        viewitems = {
        }
        return render(request, 'gst/sub_task_create.html', viewitems)

    def post(self, request):
        name = request.POST['name']
        task = request.POST['task']
        deadline = request.POST['deadline']
        if t.deadline > Task.objects.get(name=t.task).deadline:
            return HTTPr('The deadline is bigger than task mother.')
        created_datetime = request.POST['created_datetime']
        complete =
        new_sub_task = SubTask.objects.create(
            name=name,
            task=task,
            deadline=deadline,
            created_datetime=created_datetime,
            complete=complete
            )
        new_sub_task = SubTask.objects.create(user=request.user, name=n)
        return HTTPr('Successful created sub task.')

@login_required
class SubTaskView(View):
    def get(self, request):
        viewitems = {
        }
        subtasks = SubTask.objects.filter(user=request.user)
        for subtask in subtasks
            print subtask
        return render(request, 'gst/sub_task.html', {'subtasks': subtasks})

@login_required
class SubTaskDeleteView(View):
    def get(self, request):
        viewitems = {
        }
        subtasks = SubTask.objects.filter(user=request.user)
        for subtask in subtasks
            print subtask
        return render(request, 'gst/sub_task_delete.html', {'subtasks': subtasks})

    def post(self, request):
        n = request.POST['name']
        SubTask.objects.filter(name=n).filter(user=request.user).delete()
        return HTTPr('Successful deleted sub task.')

@login_required
class SubTaskEditView(View):
    def get(self, request):
        viewitems = {
        }
        subtasks = SubTask.objects.filter(user=request.user)
        for subtask in subtasks
            print subtask
        return render(request, 'gst/sub_task_modify.html', {'subtasks': subtasks, 'edit':True})

    def post(self, request):
        t = SubTask.objects.get(name=request.POST['name'])
        t.name = request.POST['new_name']
        t.deadline = request.POST['new_deadline']
        if t.deadline > Task.objects.get(name=t.task, user=request.user).deadline:
            return HTTPr('SubTask deadline should be shorter than task deadline.')
        t.complete = request.POST['new_complete']
        t.save()
        return HTTPr('Successful edited the sub task.')
