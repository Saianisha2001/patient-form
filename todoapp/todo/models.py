from django.db import models
# from datetime import datetime
from django.utils import timezone
import datetime


from django.db.models.fields import GenericIPAddressField
# Create your models here.
class Patient(models.Model):
    
    sno=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    gender=models.CharField(max_length=128)
    age=models.IntegerField(blank=True, null=True)
    disease=models.CharField(max_length=200)
    docname=models.CharField(max_length=200)
    docfee=models.IntegerField(default=500)
    date_created=models.DateTimeField(default=timezone.now, blank=True)

    def str(self):
        return self.fname+ " "+ self.lname
