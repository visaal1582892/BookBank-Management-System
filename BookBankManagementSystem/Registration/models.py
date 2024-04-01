from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    cid = models.CharField(max_length=15, primary_key=True)
    uid = models.OneToOneField(User, on_delete=models.CASCADE)
    type=models.CharField(max_length=10)
class Department(models.Model):
    did = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=50)

# Customer type
customer_type=["Librarian","Student"]

# semesters
semesters = ['1','2','3','4','5','6','7','8']

# departments
departments = Department.objects.all()