from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, primary_key=True)
    password = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class SubTask(models.Model):
	name = models.CharField(max_length=50)
	task = models.ForeignKey(Task)
	deadline = models.DateTimeField()
	complete = models.BooleanField

	def __str__(self):
		return self.name

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_leng=50, primary_key=True)

	def __str__(self):
		return self.name
