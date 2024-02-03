from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def index(request):
 # return HttpResponse('index page')
  x={'name':'fatmaa','age':'2474528458465'}
  return render(request, 'pages/index.html',x )

def about(request):
  #return HttpResponse('about page')
  return render(request, 'pages/about.html',{'name':'esraa'})

def catgory(request):
  return render(request, 'pages/catgory.html',)