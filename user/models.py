from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20,null=False,unique=True)
    pwd = models.CharField(max_length=20, null=False,unique=False)