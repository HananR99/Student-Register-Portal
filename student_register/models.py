from django.db import models

class Department(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    std_id = models.CharField(max_length=5)
    mobile= models.CharField(max_length=15)
    department= models.ForeignKey(Department,on_delete=models.CASCADE)
    
