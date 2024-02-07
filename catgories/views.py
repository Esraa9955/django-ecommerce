from django.shortcuts import render,reverse,redirect
from django.http import  HttpResponse,HttpResponseRedirect
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView,UpdateView,CreateView,DetailView,DeleteView
from django.views import View
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


class CategoryUpdategeneric(UpdateView):
  model =Category
  template_name='categories/update.html'
  context_object_name='form'
  form_class=CategoryForm
  success_url = reverse_lazy('category.all')


class CategoryDetailsgeneric(DetailView):
  model =Category
  template_name='categories/details.html'
  context_object_name='category'
  form_class=CategoryForm
  success_url = reverse_lazy('category.details')

class CategoryDeletegeneri(DeleteView):
  model =Category
  template_name='categories/delete.html'
  context_object_name='category'
  success_url = reverse_lazy('category.all')

class CategoryListgeneric(ListView):
  model =Category
  template_name='categories/list.html'
  context_object_name='categories'
  
class CategoryUpdateView(View):
  def get(self,request,id):
    print('get class based view')
    context={'form':CategoryForm(instance=Category.getcategorydetails(id))}
    return render(request,'categories/update.html',context)
  def post(self, request,id):
    print('post class based view')
    form=CategoryForm(request.POST,instance=Category.getcategorydetails(id))
    if(form.is_valid()):
      form.save()
      return redirect(reverse('category.all'))


def home(request):
  return HttpResponse('welcome ')
def categorylist(request):
  context ={'categories':Category.Getall()}
  return render(request,'categories/list.html',context)

def categoryadd(request):
    form = CategoryForm(request.POST or None)  # Instant iate the form with request.POST data if it's a POST request
    context = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            obj = form.save()
            return redirect(reverse('category.all'))
    return render(request, 'categories/add.html', context)

def CategoryUpdate(request,id):
  
  context={'form':CategoryForm(instance=Category.getcategorydetails(id))}
  if(request.method=='POST'):
    form=CategoryForm(request.POST,instance=Category.getcategorydetails(id))
    if(form.is_valid()):
      form.save()
      return redirect(reverse('category.all'))
  return render(request,'categories/update.html',context)
""" class Categorydelete(DeleteView):
    model = Category
    success_url = reverse_lazy('category.list')
    template_name = 'category/delete.html'

class CategoryCreate(CreateView):
    model = Category
    template_name = 'category/update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category.list')

class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category/index.html'
class CategoryDetails(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'category/details.html'
class CategoryUpdate(UpdateView):
    model = Category
    context_object_name = 'category'
    form_class = CategoryForm
    template_name = 'category/update.html'
    success_url = reverse_lazy('category.list')
# Create your views here.
#httprequest,return httpresponse
# categories=[
#     {'id':1,'Name':'laptop','path':'os.png'},
#     {'id':2,'Name':'smartphones','path':'iot.png'},
#     {'id':3,'Name':'clothes','path':'python.jpeg'},
#     {'id':4,'Name':'makeup','path':'php.png'},
# ]
def hellcu(request):
    return  HttpResponse('<h1>welcome to django <span style="color:green">cu</span> developers</h1>')
# def categorylist(request):
#     #return HttpResponse('<h1>Tracks list</h1>')
#     #return HttpResponse(categories)
#     context={}
#     context['categories']=categories
#     return  render(request,'category/index.html',context)
# def categorydetails(request,categoryid):
#     #print(type(categoryid))
#     #print((categoryid)+10)
#     #map,filter
#     #lambda  input:output
#     category=filter(lambda t:t['id']==categoryid,categories)
#     #return HttpResponse(f'<h1>Track info</h1></br>Track id :{categoryid}')
#     category=list(category)
#     if category:
#         return HttpResponse(category)
#     return HttpResponse('<span style="color:red">category not found</span>') """