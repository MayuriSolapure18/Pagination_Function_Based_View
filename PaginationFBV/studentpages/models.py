from django.db import models

# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=32)
    Branch=models.CharField(max_length=32)
    Age=models.IntegerField()
    Score=models.IntegerField()


    def __str__(self):
        return self.Name