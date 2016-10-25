from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse as HTTPr
from django.utils.decorators import method_decorator
from .models import *

# Create your views here.
def home(request):
    viewitems = {
        'title': 'Home',
        'username': 'Facu'
    }
    return render(request, 'gst/index.html', viewitems)

class LoginView(View):
    def get(self, request):
        viewitems = {
        }
        return render(request, 'gst/login.html', viewitems)

    def post(self, request):
        e = request.POST['email']
        p = request.POST['password']
        try:
            usuario = User.objects.get(email=e, password=p)
            return HTTPr('Bienvenido ' + usuario.name)
        except User.DoesNotExist:
            return HTTPr('El usuario o contrasena son incorrectos.')

class RegisterView(View):
    def get(self, request):
        viewitems = {
        }
        return render(request, 'gst/register.html', viewitems)

    def post(self, request):
        n = request.POST['name']
        e = request.POST['email']
        p = request.POST['password']
        new_user = User.objects.create(name = n, password = p, email = e)
        return HTTPr('Bienvenido ' + new_user.name + '. Esperamos que disfrutes del servicio.')
