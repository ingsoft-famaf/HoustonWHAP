from django.contrib import admin
from .models import User, Task, SubTask, Category

# Register your models here.
admin.site.register(User)
admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Category)
