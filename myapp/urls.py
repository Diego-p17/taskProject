from django.contrib import admin
from django.urls    import path
from .              import views

from myapp import views

urlpatterns = [
    path('', views.index),
    path('hello/<str:username>', views.hello),
    path('projects/' , views.project),
    path('tasks/', views.tasks),
    path('about/', views.about),
]
