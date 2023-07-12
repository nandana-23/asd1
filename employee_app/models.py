from django.db import models

# Create your models here.
class department(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

class role(models.Model):
    name=models.CharField(max_length=100)



class employee(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    dept=models.ForeignKey(department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role =models.ForeignKey(role,on_delete=models.CASCADE)
    phone= models.IntegerField(default=0)
    hire_date=models.DateField()

