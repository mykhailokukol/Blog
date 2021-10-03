from django.contrib import admin
from django.contrib.sessions.models import Session
from . import models


admin.site.register(models.Message)
admin.site.register(Session)
