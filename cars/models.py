from django.db import models

# Create your models here.
class Brand(models.Model):
      Brand=models.CharField(max_length=50)
      def __str__(self):
            return self.Brand
      

class Carv(models.Model):
      name=models.CharField(max_length=50)
      Brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
      image=models.ImageField()
      spf=models.TextField(max_length=200,default='model:')
      price=models.FloatField()
      def __str__(self):
            return self.name