from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122,null=True)
    phone = models.CharField(max_length=12,null=True)
    desc = models.TextField()
    date = models.DateField()
