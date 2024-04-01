from django.db import models
from Registration.models import *

class Book(models.Model):
    bid = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=60)
    bauthor = models.CharField(max_length=50,default=None)
    bdescription = models.CharField(max_length=300)
    did = models.ForeignKey(Department, on_delete=models.CASCADE)
    bsem = models.IntegerField()
    bcount = models.IntegerField()

class Order(models.Model):
    oid = models.AutoField(primary_key=True)
    cid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bid = models.ForeignKey(Book, on_delete=models.CASCADE)
    odate = models.DateField()
    duedate = models.DateField()

# borrowDays
borrowDays = 15