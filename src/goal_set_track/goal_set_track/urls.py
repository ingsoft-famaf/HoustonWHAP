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
from gst import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),

    url(r'^category/$', views.CategoryView.as_view(), name='category'),
    url(r'^category/create/$', views.CategoryCreateView.as_view(), name='category_create'),
    url(r'^category/edit/$', views.CategoryEditView.as_view(), name='category_edit'),
    url(r'^category/delete/$', views.CategoryDeleteView.as_view(), name='category_delete'),

    url(r'^category/(?P<category>[\w]+)/$', views.TaskView.as_view(), name='task'),
    url(r'^category/(?P<category>[\w]+)/task/create/$', views.TaskCreateView.as_view(), name='task_create'),
    url(r'^category/(?P<category>[\w]+)/task/(?P<task>[\w]+)/edit/$', views.TaskEditView.as_view(), name='task_edit'),
    url(r'^category/(?P<category>[\w]+)/task/delete/$', views.TaskDeleteView.as_view, name='task_delete'),

    url(r'^category/(?P<category>[\w]+)/task/(?P<task>[\w]+)/$', views.SubTaskView.as_view(), name='subtask'),
    url(r'^category/(?P<category>[\w]+)/task/(?P<task>[\w]+)/subtask/create/$', views.SubTaskCreateView.as_view(), name='subtask_create'),
    url(r'^category/(?P<category>[\w]+)/task/(?P<task>[\w]+)/subtask/(?P<subtask>[\w]+)/edit/$', views.SubTaskEditView.as_view(), name='subtask_edit'),
    url(r'^category/(?P<category>[\w]+)/task/(?P<task>[\w]+)/subtask/delete/$', views.SubTaskDeleteView.as_view, name='subtask_delete'),
]
