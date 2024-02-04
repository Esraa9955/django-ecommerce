from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from  .models import *
# Create your views here.
def products(request):
  context={'pro':Product.objects.all()}
  return render(request,'products/products.html', context)
 
def product(request, id):
    obj1=Product.objects.get(id=id)
    context={'prod':obj1}
    return render(request, 'products/product.html', context)

def productadd(request):
   if(request.method=='POST'):
      Product.objects.create(name=request.POST['tname'],
                             price=request.POST['tprice'],
                             prand= request.POST['tprand'])
      r=reverse("products")
      return HttpResponseRedirect(r)
      #return HttpResponseRedirect('/products/')
   return render(request,'products/addproduct.html')

def productdelete(request,id):
  Product.objects.filter(id=id).delete()
  r=reverse("products")
  return HttpResponseRedirect(r)
   