from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	age = models.SmallIntegerField(default=18)
	activity = models.CharField(max_length=128, null=True)
	about_text = models.TextField(null=True)
	created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return ('%s %s' % (self.first_name, self.last_name))