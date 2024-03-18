from django.db import models

class Category(models.Model):
    cateid = models.AutoField(primary_key=True)
    catename = models.CharField(max_length=30)
class Books(models.Model):
    bid = models.CharField(primary_key=True,max_length=15)
    bname = models.CharField(max_length=60)
    bauth = models.CharField(max_length=50,default=None)
    cateid = models.ForeignKey(Category,on_delete=models.CASCADE)
    bprice = models.DecimalField(max_digits=6,decimal_places=2)
    bdes = models.CharField(max_length=300)
    bavail = models.CharField(max_length=3)

# bavail values
avail=['No','Yes']

# category
cat={1 : "Fiction", 2 : "Non-Fiction", 3 : "Kids",}