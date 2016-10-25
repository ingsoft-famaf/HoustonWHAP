from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse as HTTPr
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import *
#from django.contrib.autg.decorators import login_required

# Create your views here.
def home(request):
    viewitems = {
        'title': 'Home',
        'username': 'Facu'
    }
    return render(request, 'gst/index.html', viewitems)

class LoginView(View):
    @csrf_exempt
    def get(self, request):
        viewitems = {
        }
        return render(request, 'login.html', viewitems)

    @csrf_exempt
    def post(self, request):
        e = request.POST['email']
        p = request.POST['password']
        try:
            usuario = User.objects.get(email=e, password=p)
            return HTTPr('Bienvenido ' + usuario.name)
        except User.DoesNotExist:
            return HTTPr('El usuario o contrasena son incorrectos.')

class RegisterView(View):
    @csrf_exempt
    def get(self, request):
        viewitems = {
        }
        return render(request, 'register.html', viewitems)

    @csrf_exempt
    def post(self, request):
        n = request.POST['name']
        e = request.POST['email']
        p = request.POST['password']
        print n
        print e
        print p
        new_user = User.objects.create(name = n, password = p, email = e)
        return HTTPr('Bienvenido ' + new_user.name + '. Esperamos que disfrutes del servicio.')

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
