from django.db import models

# Create your models here.
class Stu(models.Model):
    stuid = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    score = models.CharField(max_length=10)

    def __unicode__(self):
    	return self.name