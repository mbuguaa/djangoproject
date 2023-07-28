from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    admission = models.IntegerField()
    course = models.CharField(max_length=200)

    class Meta:
        db_table = "Student"
