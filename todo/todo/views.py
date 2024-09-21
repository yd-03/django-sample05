from django.views import generic
from .models import TodoModel


class TodoList(generic.ListView):
    template_name = "todo/list.html"
    model = TodoModel


class TodoDetail(generic.DetailView):
    template_name = "todo/detail.html"
    model = TodoModel
