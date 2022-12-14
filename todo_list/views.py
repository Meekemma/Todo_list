from django.shortcuts import render, redirect
from .models import *
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()

    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    

    context={'todos': todos, 'form': form}        
    return render(request, 'todo_list/view.html', context)

def deleteItem(request, pk):
    item = Todo.objects.get(id = pk)
    item.delete()
    return redirect('/')

def update(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance = todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance = todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={ 'form': form}       
    return render(request, 'todo_list/update.html', context )