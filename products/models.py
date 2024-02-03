from django.db import models

class Product(models.Model):
  name=models.CharField(max_length=100)
  content=models.TextField()
  price=models.DecimalField(max_digits=10, decimal_places=5)
  #image=models.ImageField(upload_to='photos/%y/%m/%d')
  active=models.BooleanField(default=True)
