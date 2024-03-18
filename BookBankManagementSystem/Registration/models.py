from django.db import models
from django.contrib.auth.models import User

class Customers(models.Model):
    cid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User)
# class Department(models.Model):
#     did = models.CharField(primary_key=True)
#     dname = models.CharField()
