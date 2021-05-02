from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.urls import reverse_lazy

# login and auth
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

# the model
from .models import Task

class CustomLoginView(LoginView):
    fields = "__all__"
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base_app/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] =  context["tasks"].filter(user = self.request.user)
        context["count"] =  context["tasks"].filter(task_completed = False).count()
        return context
        

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base_app/details.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title', 'desc', 'task_completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title', 'desc', 'task_completed']
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'deleted_task'
    success_url = reverse_lazy('tasks')
