from django.shortcuts import render
from .models import ToDo
def home(request):
    return render(request,'home.html')


def active_tasks(request):
    tasks = ToDo.objects.filter(active=True)
    return render(request,'active_tasks.html',{'tasks':tasks})