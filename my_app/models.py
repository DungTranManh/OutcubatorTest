import imp
from django.db import models
from datetime import datetime
import pytz
# Create your models here.

class Applicants(models.Model):
    applicant_id = models.IntegerField(primary_key=True,blank=True)
    name = models.TextField()
    email = models.EmailField()
    dob = models.DateField()
    country = models.TextField()
    status = models.TextField(default='pending')
    created_dttm = models.DateTimeField(default=datetime.now(pytz.timezone('Asia/Bangkok')))

class Results(models.Model):
    applicant_id = models.IntegerField()
    client_key = models.TextField(default="h31*(0@l4&wqqj(ix$-1&(nif!#jp68ylq@+!fo)ij9@5fmxws")
    applicant_status = models.TextField()
    processed_dttm = models.DateTimeField(default=datetime.now(pytz.timezone('Asia/Bangkok')))