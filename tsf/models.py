from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
#class customer(models.Model):
 #   acc = models.PositiveIntegerField(primary_key=True)
  #  name = models.CharField(max_length=50)
   # email = models.EmailField(max_length=100,unique=True)
    #balance = models.FloatField()
    #phone = models.PositiveIntegerField()

#class history(models.Model):
 #   sender = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='sender')
  #  receiver = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='receiver')
   # amt = models.FloatField()
    #date= models.DateTimeField(auto_now_add=True)    