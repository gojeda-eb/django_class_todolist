from django.db import models
from django.conf import settings


class Priority(models.Model):
    name = models.CharField(max_length=20)
    order = models.IntegerField()

    def __str__(self):
        return self.name


class Todo(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_assigned = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
