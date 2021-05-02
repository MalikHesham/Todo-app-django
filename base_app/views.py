from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.urls import reverse_lazy

# login and auth
from django.contrib.auth.views import LoginView

# the model
from .models import Task

class CustomLoginView(LoginView):
    fields = "__all__"
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base_app/list.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base_app/details.html'

class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'deleted_task'
    success_url = reverse_lazy('tasks')
