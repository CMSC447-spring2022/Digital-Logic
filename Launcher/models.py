from django.db import models


# Create your models here.

class LaunchContext(models.Model):
    launch_url = models.TextField()
    instance_id = models.TextField(blank=True)


class ErrorContext(models.Model):
    text = models.TextField()
