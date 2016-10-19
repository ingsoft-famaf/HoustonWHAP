from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    def authenticate(self, password):
        return self.password == password
