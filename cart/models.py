from django.db import models
from shop.models import *


class cartlist(models.Model):
    cartid=models.CharField(max_length=50,unique=True)
    dateadded=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cartid

class items(models.Model):
    prodt=models.ForeignKey(prod,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quant=models.IntegerField()
    def __str__(self):
        return self.prodt
