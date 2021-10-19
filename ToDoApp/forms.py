from django import forms
from . import models


class ToDoListForm(forms.ModelForm):

    class Meta:

        model = models.ToDoList
        fields = ['title', 'tasks', ]
        labels = {
            'title': 'Название',
            'tasks': None,
        }
