
from django.urls import path
from todo_app import views
urlpatterns = [
    path("", views.todo_list),
    path("delete/<int:id>/", views.todo_delete, name="todo-list"),
    path("create/", views.todo_create, name="todo-delete"),
    path("update/<int:id>/", views.todo_update, name="todo-update"),
]
