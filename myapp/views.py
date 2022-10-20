from ast import If
from turtle import title
from django.shortcuts   import render
from django.http        import HttpResponse, JsonResponse
from django.shortcuts   import get_object_or_404
from django.shortcuts   import render, redirect
from .models            import Project, Task
from .forms             import CreateNewTask, CreateNewProject

# Create your views here.
########################
##       Views        ##
########################


def hello(request, id):
    return HttpResponse("hello %s" %id)
#index
def index(request):
    title = 'Django course'
    return render(request ,"index.html", {'title' : title})

def about(request):
    return render(request,"about.html")
#service_projects
def project(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {'projects': projects}  )

def create_project(request):
    if request.method == 'GET':
        return render(request, "projects/create_project.html", {'form': CreateNewProject})
    else:
        Project.objects.create(name =request.POST['name'])
        return redirect('projects')

def details_project(request, id):
    project = get_object_or_404(Project,id=id)
    tasks    = Task.objects.filter(project_id =id)
    return render(request,"projects/details_project.html",{
                  'project': project,
                  'tasks': tasks,
                })
#service_tasks
def tasks(request):
    #task = Task.objects.get(id=id)
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, "tasks/task.html", {'tasks': tasks})

def create_task(request):
    if request.method == "GET":
        #return screen_create_task
        return render(request, "tasks/create_task.html", {'form': CreateNewTask})
    else:
        Task.objects.create(
            title        = request.POST['title'],
            description  = request.POST['description'],
            project_id = 2
        )
        return redirect('tasks')