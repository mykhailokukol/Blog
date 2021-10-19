from django.shortcuts import render, render, get_object_or_404
from django.views.generic import View
from . import models, forms


class IndexView(View):

    def get(self, request):
        user_todo_lists = models.ToDoList.objects.filter(author=request.user.id).order_by('-created')
        CreateListForm = forms.ToDoListForm()
        return render(request, 'ToDoApp/index.html', {
            'todo_lists': user_todo_lists,
            'CreateListForm': CreateListForm,
        })

    def post(self, request):
        pass
