from __future__ import unicode_literals

from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, default='DEFAULT')
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(default=datetime.datetime.now)
    deadline = models.DateTimeField()
    notify_user = models.BooleanField(default='False')
    complete = models.BooleanField(default='False')

    def __str__(self):
        return self.name

class SubTask(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, default='DEFAULT')
    task = models.ForeignKey(Task)
    deadline = models.DateTimeField()
    created_datetime = models.DateTimeField(default=datetime.datetime.now)
    notify_user = models.BooleanField(default='False')
    complete = models.BooleanField(default='False')


    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey('Task', related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
