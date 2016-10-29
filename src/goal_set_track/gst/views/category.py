from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse as HTTPr
from ..models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class CategoryView(LoginRequiredMixin, View):
    def get(self, req):
        viewitems = {
            'title': 'Categories',
            'username': req.user.username,
            'categories': req.user.category_set.all()
        }
        return render(req, 'gst/category.html', viewitems)

class CategoryCreateView(LoginRequiredMixin, View):
    def post(self, req):
        name = req.POST['name']
        req.user.category_set.create(name = name)
        return redirect('task', category=req.user.category_set.get(name=name).id)

class CategoryEditView(LoginRequiredMixin, View):
    def get(self, req):
        viewitems = {
        }
        categorys = Category.objects.filter(user = u)
        return render(req, 'gst/category_delete.html', {'categorys': categorys, 'edit':True})

    def post(self, req):
        oldName = req.POST['oldName']
        newName = req.POST['newName']
        Category.objects.filter(name=oldName).filter(user=u).update(name=newName)
        return HTTPr('Successful edited the category')

class CategoryDeleteView(LoginRequiredMixin, View):
    def post(self, req, category):
        req.user.category_set.get(id=category).delete()
        return redirect('category')
