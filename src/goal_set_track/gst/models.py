from __future__ import unicode_literals

from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(default=datetime.datetime.now)
    deadline = models.DateTimeField()
    complete = models.BooleanField()

    def __str__(self):
        return self.name

class SubTask(models.Model):
    name = models.CharField(max_length=50)
    task = models.ForeignKey(Task)
    deadline = models.DateTimeField()
    created_datetime = models.DateTimeField(default=datetime.datetime.now)
    complete = models.BooleanField

    def __str__(self):
        return self.name
