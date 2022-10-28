from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import Todo


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class TodoListView(ListView):
    # model = Todo

    def get_queryset(self):
        return Todo.objects.filter(user_assigned=self.request.user)


class TodoDetailView(DetailView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ['name', 'description', 'done', 'priority']
    success_url: reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)



