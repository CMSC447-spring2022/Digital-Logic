from django.db import models


# Create your models here.

class LoginContext(models.Model):
    login_url = models.TextField()
    instance_id = models.TextField(blank=True)


# class ErrorContext(models.Model):
#     text = models.TextField()
