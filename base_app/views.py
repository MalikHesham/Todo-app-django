from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base_app/list.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base_app/details.html'

