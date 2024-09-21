from django.urls import path
from .views import TodoList, TodoDetail, TodoUpdate, TodoDelete, TodoCreate

urlpatterns = [
    path("", TodoList.as_view(), name="todo_list"),
    path("todo_detail/<int:pk>/", TodoDetail.as_view(), name="todo_detail"),
    path("todo_update/<int:pk>/", TodoUpdate.as_view(), name="todo_update"),
    path("todo_delete/<int:pk>/", TodoDelete.as_view(), name="todo_delete"),
    path("todo_create/", TodoCreate.as_view(), name="todo_create"),
]
