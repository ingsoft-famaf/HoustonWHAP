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
