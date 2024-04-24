from django.db import models
from  django.utils import timezone

# Create your models here.
class CategoryStay(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    def _str_(self):
        return self.name

class Babe(models.Model):
    c_stay = models.ForeignKey(CategoryStay, on_delete=models.CASCADE, null=True, blank=True)
    # c_fee = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)
    #the above line11 links the class Babe to the class CategoryStay
    b_name = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True, default=0)
    gender = models.CharField(max_length=10, null=True, blank=True)
    location= models.CharField(max_length=10, null=True, blank=True)
    NameOfPersonBringingBabe = models.CharField(max_length=200, null=True, blank=True)
    TimeIn = models.DateTimeField(null=True, blank=True)
    TimeOut = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return self.b_name

class Payment(models.Model):
    payee = models.ForeignKey(Babe, on_delete=models.CASCADE, null=True, blank=True)
    c_payment = models.ForeignKey(CategoryStay, on_delete=models.CASCADE, null=True, blank=True)
    pay_number = models.IntegerField(null=True, blank=True, default=0)
    amount = models.IntegerField(null=True, blank=True, default=0)
    currency = models.CharField(max_length=5, default ='Shs.', null=True, blank=True)

    def _str_(self):
        return self.payee