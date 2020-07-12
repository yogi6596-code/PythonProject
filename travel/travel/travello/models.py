from django.db import models

# Create your models here.


class Destination(models.Model):

    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    # id: int
    # name: str
    # img: str
    # desc: str
    # price: int
    # offer:bool
    
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=120)
    phone=models.IntegerField()
    desc=models.TextField()
    date=models.DateField()

