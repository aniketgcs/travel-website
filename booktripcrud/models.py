from distutils.command.upload import upload
from sqlite3 import Timestamp

from django.db import models

# Create your models here.

class AdminTours(models.Model):
    placeImage=models.ImageField(upload_to="travelswebsite/static/images",default="")
    placeName=models.CharField(max_length=30,default="place-name")
    placeDescription=models.CharField(max_length=300,default="place-description")
    tourPrice=models.IntegerField(default="0")

    def __str__(self):
        return self.placeName
    
class BookTrip(models.Model):
    sNO=models.AutoField(primary_key=True) #no need to write django will create automatically
    customerName=models.CharField(max_length=50,default="customer-name")
    customerEmail=models.EmailField(max_length=50,default="customer-name")
    customerPhone=models.IntegerField(default="customer-phonenumber")
    customerAddress=models.CharField(max_length=300,default="customer-address")
    customerWhereTo=models.CharField(max_length=50,default="customer-wheretoplace")
    customerNoOfGuests=models.IntegerField(default="customer-NoOfGuests")
    customerArrivalDate=models.DateField()
    customerLeavingDate=models.DateField()
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)


    def __str__(self):
        return "Book trip request from  " + self.customerName +"-"+self.customerEmail







    


    