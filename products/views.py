from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from  .models import *
from .forms import *
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
                             prand= request.POST['tprand'],
                             image=request.FILES['timage'],
                            catgory =Category.objects.get(id=request.POST['category']))
      r=reverse("products")
      #r=reverse("products",args=[1,'as'])
      return HttpResponseRedirect(r)
      #return HttpResponseRedirect('/products/')
   context={'cat':Category.objects.all()}
   return render(request,'products/addproduct.html',context)

def productaddForm(request):
   form=ProductForm()
   context={'form':form}
   if(request.method=='POST'):
      form=ProductForm(request,request.POST,request.FILES)
      if(form.is_valid()):
         Product.objects.create(name=request.POST['tname'],
                              price=request.POST['tprice'],
                              prand= request.POST['tprand'],
                              image=request.FILES['timage'],)
         r=reverse("products")
         return HttpResponseRedirect(r)
         
      else:
         context['msg']='data not complete'
   return render(request,'products/productaddForm.html',context)

def productdelete(request,id):
  Product.objects.filter(id=id).delete()
  r=reverse("products")
  return HttpResponseRedirect(r)

def productupdate(request,id):
   
   obj2=Product.objects.get(id=id)
   obj2=Product.product(id) 
   context={'updateprod':obj2}
   if(request.method=='POST'):
      if(request.POST['tname']!='' and request.POST['tprice']!=''  and request.POST['tprand']!='' ):
         Product.objects.filter(id=id).update(name=request.POST['tname'],
                              price=request.POST['tprice'],
                              prand= request.POST['tprand'])
         r=reverse("products")
         return HttpResponseRedirect(r)
      else:
         context['msg']='kindly fill all fileds'
   return render(request,'products/updateproduct.html',context)
   
