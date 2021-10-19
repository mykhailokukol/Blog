from django.db import models
from django.contrib.auth.models import User


class ToDoList(models.Model):

    """
    To-Do List Model
    """

    title = models.CharField(max_length=128, blank=False, null=False)
    tasks = models.ManyToManyField('Task')
    created = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ('%s: %s' % (self.author, self.title))


class Task(models.Model):

    """
    To-Do List Task Model
    """

    text = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.text
