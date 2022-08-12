from django.db import models
from django.urls import reverse


# Create your models here.
class categ(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)

    def __str__(self):
        return self.name

class prod(models.Model):
    name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    img= models.ImageField(upload_to='images')
    desc=models.TextField()
    stock=models.IntegerField()
    price=models.IntegerField()
    available=models.BooleanField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)


    def __str__(self):
        return self.name