from django.db import models
categories=[
  ('phone','phone'),
  ('computer','computer'),
]
class Product(models.Model):
  name=models.CharField(max_length=100, default='name', verbose_name='title')
  content=models.TextField(null=True, blank=True, verbose_name='description')
  price=models.DecimalField(max_digits=10, decimal_places=5, default=10.0)
  #image=models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='photo')
  image = models.ImageField(upload_to='product_images', default='default_image.jpg')
  active=models.BooleanField(default=True)
  category=models.CharField(max_length=50, null=True, blank=True,choices=categories)
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name='product'
    ordering =['name']
    #ordering =['-price']
