from django.db import models
#rom datetime import datetime
from django.utils import timezone
from django.shortcuts import reverse
from catgories.models import * 
'''categories=[
  ('phone','phone'),
  ('computer','computer'),
]'''
class Product(models.Model):
  name=models.CharField(max_length=100, default='name', verbose_name='title')
  content=models.TextField(null=True, blank=True, verbose_name='description')
  price=models.DecimalField(max_digits=10, decimal_places=5, default=10.0)
  #image=models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='photo')
  image = models.ImageField(upload_to='products/images/', default='default_image.jpg',blank=True, null=True)
  active=models.BooleanField(default=True, null=True)
  #category=models.CharField(max_length=50, null=True, blank=True,choices=categories)
  created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
  updateat = models.DateTimeField(auto_now=True,null=True, blank=True)
  prand=models.CharField(max_length=50,default='', null=True)
  catgory=models.ForeignKey(Category,null=True, blank=True,on_delete=models.CASCADE )
  def __str__(self):
    return self.name
   # return self.name+' '+self.price
  @classmethod
  def products(self): 
    return self.objects.all()

  @classmethod
  def product(cls,id):
    return cls.objects.get(id=id)

  def getimageurl(self):
    return f'/media/{self.image}'
  
  def getupdateurl(self):
    return reverse('product.update',args=[self.id])
  
'''  class Meta:
    verbose_name='product'
    ordering =['name']
    #ordering =['-price']
'''