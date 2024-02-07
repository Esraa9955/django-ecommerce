from django.db import models

class Category(models.Model):
  name=models.CharField(max_length=50, unique=True)
  description=models.CharField(max_length=30,default='')
  #createat=models.DateTimeField(blank=True, null=True)

  @classmethod
  def getcategorydetails(cls,id):
    return cls.objects.get(id=id)
  @classmethod
  def Getall(cls):
    return cls.objects.all()
  @classmethod
  def getcatgory(self):
    print(self.objects.all())
    return [(t.id,t.name) for t in self.objects.all()]
  
  def __str__(self):
    return self.name