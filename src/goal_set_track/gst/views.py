from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse as HTTPr
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import *

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