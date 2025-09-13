from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    # size = models.IntegerField()
    age = models.IntegerField(default=2)
    # data = models.IntegerField(null=True, blank=True)

class Department(models.Model):
    title = models.CharField(max_length=16)

# Department.objects.create(title='销售部')

class Role(models.Model):
    caption = models.CharField(max_length=16)
