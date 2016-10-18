from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse as HTTPr
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def home(request):
    return HTTPr('Hola!')

'''
def login(request):
    # print request.method
    # TODO Render login template.
    # viewitems = {}
    # viewitems.title = 'GST Login'
    # return render(request, 'gst/login.html', viewitems)
    return HTTPr('Estas en el login.')
'''

class LoginView(View):
    @csrf_protect
    def get(self, request):
        viewitems = {
        }
        return render(request, 'login.html', viewitems)

    def post(self, request):
        print request.POST

