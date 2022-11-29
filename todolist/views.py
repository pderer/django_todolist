from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Todo
from django.core.paginator import Paginator
from .forms import TodoForm


# Create your views here.
def index(request):
    page = request.GET.get('page', '1')
    latest_todo_list = Todo.objects.order_by('-pub_date')
    paginator = Paginator(latest_todo_list, 10)
    page_obj = paginator.get_page(page)
    context = {'latest_todo_list' : page_obj, 'is_modify' : False}
    return render(request, 'todolist/index.html', context)

def todo_create(request):
    todo = Todo(todo_text=request.POST.get('content'), pub_date=timezone.now())
    todo.save()
    return redirect('index')


def todo_modify(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    page = request.GET.get('page', '1')
    latest_todo_list = Todo.objects.order_by('-pub_date')
    paginator = Paginator(latest_todo_list, 10)
    page_obj = paginator.get_page(page)
    context = {'latest_todo_list' : page_obj, 'is_modify' : True , 'prev_todo_text' : todo}
    return render(request, 'todolist/index.html', context)

def todo_modify_save(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.todo_text = request.POST.get('content')
    todo.save()
    return redirect('index')

def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('index')
    