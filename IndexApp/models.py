from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=32, null=True)
    birth_date = models.DateField(null=True)
    activity = models.CharField(max_length=128, null=True)
    about_text = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    photo = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return ('%s %s' % (self.user.first_name, self.user.last_name))


# Создание объекта модели Profile во время создания нового пользователя
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Post(models.Model):

    title = models.CharField(
        max_length=128, unique=True, default='Название поста')
    text = models.TextField(null=True, default='Текст поста')
    likes = models.ManyToManyField(User, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    edited = models.DateTimeField(auto_now_add=False, auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='Автор', default=None)

    def __str__(self):
        return self.title


class PostComment(models.Model):

    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=128, null=False,
                            blank=False, default='Ваш комментарий')

    def __str__(self):
        return 'Пост: %s, Пользователь: %s, Текст: %s' % (self.post, self.user, self.text)
