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
        return render(request, 'gst/login.html', viewitems)

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
        return render(request, 'gst/register.html', viewitems)

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

class CategoryNewView(View):
    @csrf_exempt
    def get(self, request):
        viewitems = {
        }
        return render(request, 'gst/category.html', viewitems)

    @csrf_exempt
    def post(self, request):
        return HTTPr('Estas aca ASD.')
