from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	location = models.CharField(max_length=32, null=True)
	birth_date = models.DateField(null=True)
	activity = models.CharField(max_length=128, null=True)
	about_text = models.TextField(null=True)
	created = models.DateTimeField(auto_now_add=True, null=True)
	photo = models.ImageField(upload_to='staticfiles/images/', null=True, blank=True)

	def __str__(self):
		return ('%s %s' % (self.user.first_name, self.user.last_name))

# Создание объекта модели Profile во время создания нового пользователя
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)