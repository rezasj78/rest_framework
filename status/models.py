from django.db import models
from django.contrib.auth.models import User


def upload_to_image(instance, filename):
    return 'status/{filename}'.format(user=instance, filename=filename)


class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


class Status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='media/', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = StatusManager()

    def __str__(self):
        return str(self.content[:50])

    def get_user_name(self):
        return self.user.username

    class Meta:
        verbose_name = 'status post'
        verbose_name_plural = 'status posts'
