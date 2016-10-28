"""goal_set_track URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from gst import login_view, task_view, subtask_view, category_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_view.home, name='home'),
    url(r'^login/$', login_view.LoginView.as_view(), name='login'),
    url(r'^logout/$', login_view.LogoutView.as_view(), name='logout'),
    url(r'^register/$', login_view.RegisterView.as_view(), name='register'),

    url(r'^category/$', category_view.CategoryView.as_view(), name='category'),
    url(r'^category/create/$', category_view.CategoryCreateView.as_view(), name='category_create'),
    url(r'^category/edit/$', category_view.CategoryEditView.as_view(), name='category_edit'),
    url(r'^category/delete/$', category_view.CategoryDeleteView.as_view(), name='category_delete'),

    url(r'^category/(?P<category>[\w]+)/$', task_view.TaskView.as_view(), name='task'),
    url(r'^category/(?P<category>[\w]+)/task/create/$', task_view.TaskCreateView.as_view(), name='task_create'),
    url(r'^category/(?P<category>[\w]+)/task/(?P<task>[\w]+)/edit/$', task_view.TaskEditView.as_view(), name='task_edit'),
    url(r'^category/(?P<category>[\w]+)/task/delete/$', task_view.TaskDeleteView.as_view, name='task_delete'),

    url(r'^category/(?P<category>[\w]+)/task/(?P<task>[\w]+)/$', subtask_view.SubTaskView.as_view(), name='subtask'),
    url(r'^category/(?P<category>[\w]+)/task/(?P<task>[\w]+)/subtask/create/$', subtask_view.SubTaskCreateView.as_view(), name='subtask_create'),
    url(r'^category/(?P<category>[\w]+)/task/(?P<task>[\w]+)/subtask/(?P<subtask>[\w]+)/edit/$', subtask_view.SubTaskEditView.as_view(), name='subtask_edit'),
    url(r'^category/(?P<category>[\w]+)/task/(?P<task>[\w]+)/subtask/delete/$', subtask_view.SubTaskDeleteView.as_view, name='subtask_delete'),
]
