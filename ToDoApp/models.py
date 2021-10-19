from django.db import models
from django.contrib.auth.models import User


class ToDoList(models.Model):

    """
    To-Do List Model
    """

    title = models.CharField(max_length=128, blank=True, null=True)
    tasks = models.ManyToManyField('Task')
    created = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.title is not None:
            return ('%s: %s' % (self.author, self.title))
        return ('%s: id - %s' % (self.author, self.pk))


class Task(models.Model):

    """
    To-Do List Task Model
    """

    text = models.CharField(max_length=255, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.text
