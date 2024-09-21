from django.views import generic
from .models import TodoModel
from django.urls import reverse_lazy


class TodoList(generic.ListView):
    template_name = "todo/list.html"
    model = TodoModel


class TodoDetail(generic.DetailView):
    template_name = "todo/detail.html"
    model = TodoModel


class TodoUpdate(generic.UpdateView):
    template_name = "todo/update.html"
    model = TodoModel
    fields = ("title", "content", "deadline")
    success_url = reverse_lazy("list")
