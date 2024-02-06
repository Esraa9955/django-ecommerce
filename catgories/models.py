from django.db import models

class Category(models.Model):
  name=models.CharField(max_length=50)
  
  @classmethod
  def getcatgory(self):
      return [(t.id,t.name) for t in self.objects.all()]