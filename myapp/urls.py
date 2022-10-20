from django.contrib import admin
from django.urls    import path
from .              import views

from myapp import views

urlpatterns = [
    path('', views.index , name ='index'),
    #information
    path('hello/<str:username>', views.hello , name = 'hello'),
    path('about/', views.about , name = 'about'),

    #Projects
    path('projects/' , views.project, name = 'projects'),
    path('create_project/', views.create_project, name = 'create_project'),
    path('project/<int:id>',views.details_project, name = 'details_project'),

    #Task Projects
    path('tasks/', views.tasks, name = 'tasks'),
    path('create_task/', views.create_task, name = 'create_task'),

]
