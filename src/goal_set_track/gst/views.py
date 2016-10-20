from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse as HTTPr
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import *

# Create your views here.
def home(request):
    return HTTPr('Hola!')

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
