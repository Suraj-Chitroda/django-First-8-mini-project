from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
# Create your views here.


def index_exp(request):
    if(request.method == 'POST'):
        form = TodoForm(request.POST)

        if(form.is_valid()):
            new_todo = Todo(todoname=request.POST['text'])
            new_todo.save()
            return redirect('index')
        else:
            return HttpResponse("Not valid form")

    else:
        todo_list = Todo.objects.order_by('id')
        form = TodoForm()
        context = {'todo_list': todo_list, 'todo_form': form}

        return render(request, 'index.html', context)


def complete(request, td_id):
    mytodo = Todo.objects.get(pk=td_id)
    mytodo.completed = True
    mytodo.save()
    return redirect('index')


def delete(request):
    mytodo = Todo.objects.filter(completed__exact=True)
    mytodo.delete()
    return redirect('index')
