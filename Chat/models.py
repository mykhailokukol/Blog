from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    text = models.TextField(null=False, blank=False)
    sent = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    edited = models.DateTimeField(auto_now=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Chat/messages/imgs', null=True, blank=True)

    def __str__(self):
        return ('%s, %s: %s..' % (self.sent, self.author, self.text[0:15]))
