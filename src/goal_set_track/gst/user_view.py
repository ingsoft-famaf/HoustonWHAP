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
