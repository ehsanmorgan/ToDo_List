from django.shortcuts import render
from .models import ToDo

# Create your views here.



def todolist(request):
    return render(request,'todo/todolist.html',{})