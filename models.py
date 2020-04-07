from django.db import models

class Patient(models.Model):
    national_id=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    address=models.TextField()
    phone_number=models.CharField(max_length=11)
    

# Create your models here.
