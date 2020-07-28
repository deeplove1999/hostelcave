from django.db import models


# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    maplink = models.URLField(max_length=200)
    phone = models.CharField(max_length=20)
    des =  models.BooleanField(default=False)
    dev = models.BooleanField(default=False)


    
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=500)