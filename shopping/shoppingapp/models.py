from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=50)
    datails=models.CharField(max_length=500)
    date=models.DateField()
    is_deleted=models.CharField(max_length=10)
    def __str__(self):
        return self.title

class Course(models.Model):
    cname=models.CharField(max_length=50)
    cdur=models.IntegerField()
    ccat=models.CharField(max_length=50)
    cprice=models.IntegerField()
    is_deleted=models.CharField(max_length=10)

    # objs=models.Manager()

class stu(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    marks=models.IntegerField()
    # def __str__(self):
    #     return self.address

class student(models.Model):
    names=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=100)

    # def __str__(self):
    #     return self.names
