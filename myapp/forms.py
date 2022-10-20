#import django forms
from django import forms


class CreateNewTask(forms.Form):
    title       = forms.CharField(label = "Task Title", max_length = 200, widget=forms.TextInput(attrs={'class': 'input_form'}))
    description = forms.CharField(label = "Task Description", max_length = 200, widget=forms.Textarea(attrs={'class': 'input_form'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label = "Project Name", max_length = 200, widget=forms.TextInput(attrs={'class': 'input_form'}))