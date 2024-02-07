from django import forms
from .models import *
from  catgories.models import *
from django.core.exceptions import ValidationError
from catgories.models import Category
class ProductForm(forms.Form):
  name=forms.CharField(max_length=3, required=True)
  price = forms.DecimalField(max_digits=10, decimal_places=5, initial=10.0)
  prand = forms.CharField(max_length=50, required=False, initial='')
  category = forms.ChoiceField(choices=[])

  #catgory=forms.ChoiceField(choices=Category.getcatgory())
  #image = forms.ImageField(upload_to='products/images/', default='default_image.jpg',blank=True, null=True)
  #content = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}), label='Description')
  #active = forms.BooleanField(initial=True, required=False)
  #category = forms.CharField(max_length=50, required=False, widget=forms.Select(choices=categories))
  
  '''def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = Category.getcatgory()
'''
  def clean_name(self):
    userentername=self.cleaned_data['name']
    obj=Product.objects.get(name=userentername).exsists()
    if obj:
        raise ValidationError('name must be unique')
    else:
       return True
    
'''
  def clean_name(self):
      user_entered_name = self.cleaned_data['name']
      try:
          Product.objects.get(name=user_entered_name)
          raise ValidationError('Name must be unique')
      except ObjectDoesNotExist:
          return user_entered_name'''