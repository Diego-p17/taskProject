from turtle import title
from django.shortcuts   import render
from django.http        import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models            import Project, Task

# Create your views here.

def index(request):
    title = 'Django course'
    return render(request ,"index.html", {'title' : title})

def hello(request, id):
    return HttpResponse("hello %s" %id)

def about(request):
    return render(request,"about.html")

def tasks(request):
    #task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, "task.html", {'tasks': tasks})

def project(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects.html", {'projects': projects}  )