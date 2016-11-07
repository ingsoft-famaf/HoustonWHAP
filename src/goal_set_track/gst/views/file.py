from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from ..models import *
from ..forms import DocumentForm

def model_form_upload(request, category, task):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('task', category=category, task=task)
    else:
        form = DocumentForm()
    return render(request, 'gst/model_form_upload.html', {
        'form': form
    })