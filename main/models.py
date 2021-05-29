from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ResultProfile(models.Model):
    ERP = models.IntegerField()
    SEM = models.IntegerField()
    SUBJECT_NAME1 = models.CharField(max_length=100)
    SUBJECT_NAME2 = models.CharField(max_length=100)
    SUBJECT_NAME3 = models.CharField(max_length=100)
    SUBJECT_NAME4 = models.CharField(max_length=100)
    SUBJECT_NAME5 = models.CharField(max_length=100)
    MARK1=models.IntegerField()
    MARK2=models.IntegerField()
    MARK3=models.IntegerField()
    MARK4=models.IntegerField()
    MARK5=models.IntegerField()
    BRANCH = models.CharField(max_length=60)
    ROLL_NO = models.CharField(max_length=10)

    def __str__(self):
        return self.ROLL_NO