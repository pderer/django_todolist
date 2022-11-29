from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.todo_create, name='todo_create'),
    path('modify/<int:todo_id>/', views.todo_modify, name='todo_modify'),
    path('modify/save/<int:todo_id>', views.todo_modify_save, name='todo_modify_save'),
    path('delete/<int:todo_id>', views.todo_delete, name="todo_delete")
]