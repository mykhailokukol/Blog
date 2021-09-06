from django.contrib import admin
from IndexApp import models as index_models

# Register your models here.
admin.site.register(index_models.Profile)
admin.site.register(index_models.Post)
